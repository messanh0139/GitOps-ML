import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from joblib import dump

X_train = pd.read_csv("data/X_train.csv")
y_train = pd.read_csv("data/y_train.csv").values.ravel()

model = RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1)
model.fit(X_train, y_train)

dump(model, "model/model.joblib")