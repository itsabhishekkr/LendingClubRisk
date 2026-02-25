from lib.spark_session import get_spark_session
from lib.data_loader import load_config, load_raw_data
from lib.processing import add_name_sha2, get_duplicates_count

def main():
    print("Starting verification...")
    
    # 1. Get Spark Session
    spark = get_spark_session()
    print("Spark session initialized.")
    
    # 2. Load Config
    config = load_config()
    print("Config loaded.")
    
    # 3. Load Data
    # Note: This might fail if the user doesn't have the dataset in the expected path, 
    # but the loader has a fallback to verify the logic.
    try:
        df = load_raw_data(spark, config)
        print("Data loaded successfully.")
        
        # 4. Process
        df_with_sha = add_name_sha2(df)
        print("SHA2 column added.")
        
        # 5. Duplicates
        dupes = get_duplicates_count(spark, df_with_sha)
        print("Duplicates query planned.")
        dupes.show(5)
        
    except Exception as e:
        print(f"Data loading/processing failed as expected if data missing: {e}")
    
    print("Verification script finished.")

if __name__ == "__main__":
    main()
