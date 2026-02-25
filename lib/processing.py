from pyspark.sql.functions import sha2, concat_ws

def add_name_sha2(df):
    cols = [
        "emp_title", "emp_length", "home_ownership", "annual_inc", 
        "zip_code", "addr_state", "grade", "sub_grade", "verification_status"
    ]
    return df.withColumn("name_sha2", sha2(concat_ws("||", *cols), 256))

def get_duplicates_count(spark, df):
    df.createOrReplaceTempView("temp_table")
    result = spark.sql("""
        select name_sha2, count(*) as total_cnt 
        from temp_table 
        group by name_sha2 
        having total_cnt > 1 
        order by total_cnt desc
    """)
    return result
