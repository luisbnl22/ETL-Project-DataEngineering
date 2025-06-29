import pandas as pd

def clean_data():
    df = pd.read_csv("etl/data/input.csv")
    df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]
    df.dropna(inplace=True)
    df.to_csv("etl/data/cleaned.csv", index=False)
