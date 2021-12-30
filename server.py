from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from get_ml_prediction import get_ml_prediction

app = FastAPI()


class MLInput(BaseModel):
    text: str

@app.get("/")
def send_prediction(ml_input: MLInput):
    prediction = get_ml_prediction(ml_input.text)
    return {
        "prediction": prediction
    }
