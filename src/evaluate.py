from src.data_processing import load_data, split_data
from src.model import load_model
from sklearn.metrics import classification_report, roc_auc_score

DATA_PATH = "data/card_transdata.csv"
MODEL_PATH = "models/model.pkl"

def main():
    df = load_data(DATA_PATH)
    X_train, X_test, y_train, y_test = split_data(df)

    model = load_model(MODEL_PATH)

    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)[:,1]

    print("ROC-AUC:", roc_auc_score(y_test, y_proba))
    print(classification_report(y_test, y_pred))

if __name__ == "__main__":
    main()
