<<<<<<< HEAD
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
=======
# LendingClubRisk Data Engineering

A modular, enterprise-grade data engineering pipeline for processing LendingClub risk data using PySpark.

## 🚀 Overview

This project has been refactored from a monolithic notebook structure into a modular architecture following production-grade software engineering principles. It features decentralized configuration, structured logging, automated testing, and isolated dependency management.

## 📁 Project Structure

```text
.
├── config/             # Configuration management (YAML)
│   └── config.yaml     # Spark and data path settings
├── data/               # Local data storage
├── lib/                # Modular logic
│   ├── data_loader.py  # Data ingestion utilities
│   ├── logger.py       # Enterprise logging framework
│   ├── processing.py   # Data transformation logic
│   └── spark_session.py# SparkSession management
├── tests/              # Automated unit tests (Pytest)
├── Pipfile             # Dependency management (Pipenv)
├── verify_setup.py     # End-to-end integration verification
└── README.md           # Project documentation
```

## 🛠️ Setup

### Prerequisites
- Python 3.12+
- Apache Spark (with PySpark)
- Pipenv (`pip install pipenv`)

### Installation
Initialize the isolated environment and install dependencies:
```bash
pipenv install
```

## 💻 Usage

### Initializing Spark & Loading Data
```python
from lib.spark_session import get_spark_session
from lib.data_loader import load_config, load_raw_data

# Get Spark session initialized from config
spark = get_spark_session()

# Load project configuration
config = load_config()

# Load data with automatic fallback to local paths
df = load_raw_data(spark, config)
```

### Logging
The project utilizes a structured logging framework (Log4j style). Log messages follow the format: `TIMESTAMP - LEVEL - NAME - MESSAGE`.

### Running Verification
Verify the entire setup (Spark initialization + Data Loading + Transformations):
```bash
pipenv run python verify_setup.py
```

## 🧪 Testing

The project includes a comprehensive Pytest suite. Spark sessions are managed via global fixtures for performance.

```bash
# Run all tests
pipenv run python -m pytest

# Run only Spark-integrated tests
pipenv run python -m pytest -m spark
```

## 🌟 Key Features

- **Decentralized Configuration**: All environment specifics are managed in `config/config.yaml`.
- **Enterprise Logging**: INFO, WARN, and ERROR levels for production monitoring.
- **Isolated Environments**: Pipenv ensures consistent dependency management across Dev/Stage/Prod.
- **Modular Data Logic**: Pure Python library for core transformations, making them testable and reusable.
>>>>>>> 0aa3956 (add code are added)
