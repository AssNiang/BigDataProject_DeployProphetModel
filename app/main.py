from fastapi import FastAPI
from app.model.model import predict_next_3_hours_temp
from app.model.model import __version__ as model_version


app = FastAPI()

@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}


@app.get("/predict-next-3-hours-temp")
def predict():
    next_3_hours_temp = predict_next_3_hours_temp()
    return {"next_3_hours_temp": eval(next_3_hours_temp)}
