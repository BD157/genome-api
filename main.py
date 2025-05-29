from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from utils import process_sequence, classify_sequence

app = FastAPI()

class SequenceRequest(BaseModel):
    sequence: str

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.post("/cluster")
def cluster(data: SequenceRequest):
    try:
        return {"cluster": process_sequence(data.sequence)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/classify")
def classify(data: SequenceRequest):
    try:
        return {"lineage": classify_sequence(data.sequence)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
