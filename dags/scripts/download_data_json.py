import requests
import os
import json
import datetime as dt

def save_json(json_file):
    date_str = dt.datetime.today().strftime("%Y-%m-%d")

    with open(f'/opt/airflow/data/extraction_{date_str}.json', 'w') as f:
        json.dump(json_file, f)


def download_data_json():

    url = "https://data.cityofchicago.org/resource/85ca-t3if.json"

    # Optional: Filter by crash date (e.g., last 7 days)
    params = {
        "$where": "crash_date >= '2024-06-21T00:00:00'",
        "$order": "crash_date DESC"
    }

    response = requests.get(url, params=params)
    data = response.json()

    save_json(data)
