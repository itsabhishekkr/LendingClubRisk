import pytest
from lib.processing import add_name_sha2

@pytest.mark.spark
def test_add_name_sha2(spark):
    # Prepare sample data
    data = [
        ("Lead", "10+ years", "MORTGAGE", 50000.0, "123x", "PA", "C", "C4", "Not Verified"),
        ("Eng", "5 years", "RENT", 60000.0, "456x", "NY", "B", "B2", "Verified")
    ]
    columns = [
        "emp_title", "emp_length", "home_ownership", "annual_inc", 
        "zip_code", "addr_state", "grade", "sub_grade", "verification_status"
    ]
    df = spark.createDataFrame(data, columns)
    
    # Execute transformation
    df_transformed = add_name_sha2(df)
    
    # Assertions
    assert "name_sha2" in df_transformed.columns
    assert df_transformed.count() == 2
    
    # Check if hashes are unique for different inputs
    hashes = [row.name_sha2 for row in df_transformed.collect()]
    assert len(set(hashes)) == 2
