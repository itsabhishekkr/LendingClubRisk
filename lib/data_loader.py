import yaml
from lib.logger import get_logger

logger = get_logger(__name__)

def load_config(config_path='config/config.yaml'):
    try:
        with open(config_path, 'r') as f:
            return yaml.safe_load(f)
    except Exception as e:
        logger.error(f"Failed to load config from {config_path}: {e}")
        raise

def load_raw_data(spark, config):
    data_config = config.get('data', {})
    raw_path = data_config.get('raw_path')
    
    logger.info(f"Attempting to load data from {raw_path}")
    # Try raw path first, then local if available
    try:
        df = spark.read \
            .format("csv") \
            .option("InferSchema", "true") \
            .option("header", "true") \
            .load(raw_path)
        logger.info("Raw data loaded successfully from primary path.")
    except Exception as e:
        logger.warning(f"Could not load data from {raw_path}, trying local path... Error: {e}")
        local_path = data_config.get('local_sample_path')
        df = spark.read \
            .format("csv") \
            .option("InferSchema", "true") \
            .option("header", "true") \
            .load(local_path)
        logger.info(f"Data loaded successfully from local path: {local_path}")
            
    return df
