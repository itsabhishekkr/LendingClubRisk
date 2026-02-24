# Lending Club Risk Analysis & Data Engineering Pipeline

## Project Overview
This project involves building an end-to-end **Data Engineering pipeline** to process **1.7 GB of financial data (2.2M+ records)** from Lending Club.  
The goal is to ingest, clean, and analyze borrower data to automate **loan risk assessment** using **PySpark**.

## Data Architecture
The pipeline follows a **modular ETL (Extract, Transform, Load)** pattern:

- **Ingestion**: Raw CSV files are ingested into the data lake.  
- **Processing**: PySpark is used for heavy-duty transformations and performance tuning.  
- **Storage**: Processed data is stored in **Parquet format** for efficient querying.  
- **Persistence**: External **Hive Tables** are built on top of cleaned data for downstream analytics.

## Key Features & Logic
- **Security & Integrity**: Generated unique `emp_id` using **SHA-2 hashing** on 9 borrower attributes to handle duplicate records.  
- **Data Cleaning**: Handled missing values (e.g., filling `emp_length` with averages) and standardized formats for state codes and loan purposes.  
- **Risk Scoring**: Weighted calculation engine:  
  - **Payment History (20%)**: Based on last and total payment amounts  
  - **Defaulters History (45%)**: Includes delinquency, public records, bankruptcies  
  - **Financial Health (35%)**: Evaluates home ownership, funded amount, and grade points  

## Technology Stack
- **Language**: Python 3.10+  
- **Framework**: Apache Spark (PySpark)  
- **Environment**: Pipenv, Pyenv  
- **Testing**: Pytest  
- **Storage**: HDFS, Hive, Parquet  
- **Logging**: Log4j  

## Testing & Quality
- **Unit Testing**: Uses Pytest for modular functions.  
- Run all tests:  
  ```bash
  python -m pytest -v
