import pandas as pd
from utils.config import SELECTED_COLUMNS

def map_inputs_to_df(user_inputs):
    ordered_inputs = [user_inputs[col] for col in SELECTED_COLUMNS]
    input_df = pd.DataFrame([ordered_inputs], columns=SELECTED_COLUMNS)
    return input_df
