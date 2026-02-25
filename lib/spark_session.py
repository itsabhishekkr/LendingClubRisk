from pyspark.sql import SparkSession
import getpass
import yaml
import os
from lib.logger import get_logger

logger = get_logger(__name__)

def get_spark_session(config_path='config/config.yaml'):
    # Load config
    logger.info(f"Initializing Spark session with config: {config_path}")
    try:
        with open(config_path, 'r') as f:
            config = yaml.safe_load(f)
    except Exception as e:
        logger.error(f"Error loading config file: {e}")
        raise
    
    spark_config = config.get('spark', {})
    username = getpass.getuser()
    warehouse_dir = spark_config.get('warehouse_dir', f"/user/{username}/warehouse").replace("{username}", username)
    
    builder = SparkSession.builder \
        .appName(spark_config.get('app_name', 'SparkApp')) \
        .config('spark.ui.port', spark_config.get('ui_port', '0')) \
        .config("spark.sql.warehouse.dir", warehouse_dir) \
        .config('spark.shuffle.useOldFetchProtocol', spark_config.get('shuffle_fetch_protocol', 'true'))
    
    if spark_config.get('enable_hive', False):
        logger.info("Enabling Hive support")
        builder = builder.enableHiveSupport()
    
    master = spark_config.get('master', 'local[*]')
    logger.info(f"Setting Spark master to: {master}")
    spark = builder.master(master).getOrCreate()
    logger.info("Spark session created successfully.")
    return spark

if __name__ == "__main__":
    # Test session creation
    spark = get_spark_session()
    logger.info(f"Spark Session ID: {spark.sparkContext.applicationId}")
