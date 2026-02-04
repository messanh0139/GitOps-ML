import pandas as pd
from joblib import load
from sklearn.metrics import classification_report
import json

X_test = pd.read_csv("data/X_test.csv")
y_test = pd.read_csv("data/y_test.csv")

model = load("model/model.joblib")
predictions = model.predict(X_test)

cr = classification_report(y_test, predictions)

with open("metrics.json", "w") as f:
    json.dump({"accuracy": cr}, f)