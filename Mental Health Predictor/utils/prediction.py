def predict_risk(model, input_df):
    prediction = model.predict(input_df)[0]
    return prediction
