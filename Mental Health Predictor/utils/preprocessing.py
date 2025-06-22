import pandas as pd
from sklearn.preprocessing import LabelEncoder
from utils.config import SELECTED_COLUMNS, LABEL_COLUMN

def preprocess_data(filepath):
    df = pd.read_csv(filepath)

    df = df[SELECTED_COLUMNS + [LABEL_COLUMN]].dropna()

    le_dict = {}
    for col in SELECTED_COLUMNS + [LABEL_COLUMN]:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        le_dict[col] = le

    return df, le_dict
