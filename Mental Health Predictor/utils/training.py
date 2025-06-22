from sklearn.tree import DecisionTreeClassifier
from utils.config import LABEL_COLUMN

def train_model(df):
    X = df.drop(LABEL_COLUMN, axis=1)
    y = df[LABEL_COLUMN]

    model = DecisionTreeClassifier()
    model.fit(X,y)

    return model