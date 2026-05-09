from airflow import DAG
from datetime import datetime, timedelta

from src.extract import extract_stocks_data
from src.transform import transform_stocks_data
from src.load import load_stocks_data

from dotenv import load_dotenv
load_dotenv()

default_args = {
    "owner": "airflow",
    "start_date": datetime(2026, 5, 9),
    "retries": 3,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id = "stocks_etl_pipeline",
    default_args = default_args,
    schedule = "@daily",
    catchup=False) as dag:
    ### DAG WORKFLOW -> ETL Pipeline

    stocks_data = extract_stocks_data()
    transformed_data = transform_stocks_data(stocks_data)
    loaded_data = load_stocks_data(transformed_data) 











