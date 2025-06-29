from airflow import DAG
from airflow.operators.python import PythonOperator
from scripts.download_data_json import download_data_json
from datetime import datetime, timedelta
import requests
import os
import json
import datetime as dt



with DAG(
    dag_id="daily_crashes_import",
    start_date=datetime(2025, 6, 1),
    schedule_interval="@daily",
    catchup=False,
    description="DAG to download daily crash data in JSON format"
) as dag:

    t1 = PythonOperator(
        task_id="download_data_json",
        python_callable=download_data_json       
    )

    # Add more tasks and dependencies as needed
    # Example: t1 >> t2