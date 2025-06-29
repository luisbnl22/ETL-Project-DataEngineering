from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
from pathlib import Path

app = FastAPI()

# Path to your JSON file
DATA_FILE = Path("./data/extraction_2025-06-29.json")

@app.get("/data")
def get_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
        return JSONResponse(content=data)
    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

@app.get("/")
def read_root():
    return {"message": "Hello World"}