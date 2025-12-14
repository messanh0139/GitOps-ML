from src.data_processing import load_data, split_data
from src.model import build_pipeline, save_model
from sklearn.metrics import roc_auc_score, average_precision_score
import os

DATA_PATH = "data/card_transdata.csv"
MODEL_PATH = "models/model.pkl"

def main():
    print("📥 Loading data...")
    df = load_data(DATA_PATH)

    print("🔀 Splitting data...")
    X_train, X_test, y_train, y_test = split_data(df)

    print("🧠 Training model...")
    pipeline = build_pipeline()
    pipeline.fit(X_train, y_train)

    print("📊 Evaluating...")
    y_proba = pipeline.predict_proba(X_test)[:, 1]
    roc = roc_auc_score(y_test, y_proba)
    pr = average_precision_score(y_test, y_proba)

    print(f"ROC-AUC : {roc:.4f}")
    print(f"PR-AUC  : {pr:.4f}")

    os.makedirs("models", exist_ok=True)
    save_model(pipeline, MODEL_PATH)

    print("✅ Model saved")

if __name__ == "__main__":
    main()
