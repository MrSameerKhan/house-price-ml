from fastapi import FastAPI
import pickle
import numpy as np

app = FastAPI(title="House Price Prediction API")

# Load model once at startup
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.get("/")
def health():
    return {"status": "API is running"}

@app.post("/predict")
def predict(area: float):
    prediction = model.predict(np.array([[area]]))
    return {
        "area": area,
        "predicted_price": float(prediction[0])
    }
