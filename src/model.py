from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

def build_pipeline(random_state=42):
    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=12,
        class_weight="balanced",
        random_state=random_state,
        n_jobs=-1
    )

    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", model)
    ])
    return pipeline

def save_model(model, path):
    joblib.dump(model, path)

def load_model(path):
    return joblib.load(path)
