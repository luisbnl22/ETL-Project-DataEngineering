import os
import requests

def download_csv():
    url = "https://people.sc.fsu.edu/~jburkardt/data/csv/hw_200.csv"
    os.makedirs("data", exist_ok=True)
    response = requests.get(url)
    with open("data/input.csv", "wb") as f:
        f.write(response.content)
    print("CSV downloaded.")
