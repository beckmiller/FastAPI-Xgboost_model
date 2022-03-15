import uvicorn
from fastapi import FastAPI
from BodyPerformances import BodyPerformance
import pickle
import pandas as pd
from db import insert_data

app = FastAPI()

with open("model.pkl", "rb") as pickle_in:
    model = pickle.load(pickle_in)


@app.post("/predict")
def predict_class(data: BodyPerformance):
    data = data.dict()
    test_data = pd.DataFrame([data])
    predicted_class = model.predict(test_data)
    classes = {"A": 1, "B": 2, "C": 3, "D": 4}

    predicted = None

    for key, value in classes.items():
        if value == predicted_class:
            predicted = key

    insert_data(data, predicted)
    
    return f"Participant belongs to class {predicted}"

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
