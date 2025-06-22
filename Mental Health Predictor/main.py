import streamlit as st
from utils.config import SELECTED_COLUMNS, TARGET_LABELS, LABEL_COLUMN
from utils.preprocessing import preprocess_data
from utils.training import train_model
from utils.helpers import map_inputs_to_df
from utils.prediction import predict_risk
from utils.recommendations import get_advice



df, encoders = preprocess_data("data/survey.csv")
model = train_model(df)

st.set_page_config(page_title="Mental Health Risk Prediction", layout="centered")

st.title("Mental Health Risk Checker")
st.markdown("Answer the following questions to get your mental health risk prediction and personalized advice.")



user_input = {}
for col in SELECTED_COLUMNS:
    le = encoders[col]
    st_value = st.selectbox(f"{col.replace('_', ' ').capitalize()}:", le.classes_)
    user_input[col] = st_value



if st.button("Check Risk"):
    input_df = map_inputs_to_df(user_input)
    for col in SELECTED_COLUMNS:
        le = encoders[col]
        input_df[col] = le.transform([user_input[col]])
    result = predict_risk(model, input_df)
    st.subheader("Prediction Result:")
    st.success(f"You are {TARGET_LABELS[result]}.")
    st.markdown("### Personalized Recommendations:")
    advice_list = get_advice(user_input)
    for tip in advice_list:
        st.info(tip)
