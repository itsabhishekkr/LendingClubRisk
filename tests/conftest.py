import pytest
from pyspark.sql import SparkSession

@pytest.fixture(scope="session")
def spark():
    """
    Fixture for creating a SparkSession with session scope.
    """
    spark = SparkSession.builder \
        .appName("Pytest-SparkSession") \
        .master("local[*]") \
        .getOrCreate()
    yield spark
    spark.stop()
