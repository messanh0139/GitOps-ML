import pandas as pd
from sklearn.model_selection import train_test_split

TARGET = "fraud"

def load_data(path: str) -> pd.DataFrame:
    return pd.read_csv(path)

def split_data(df: pd.DataFrame, test_size=0.2, random_state=42):
    X = df.drop(columns=[TARGET])
    y = df[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y,
        test_size=test_size,
        stratify=y,
        random_state=random_state
    )
    return X_train, X_test, y_train, y_test
