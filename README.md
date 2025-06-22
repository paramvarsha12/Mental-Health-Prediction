# Mental-Health-Prediction
Predicts a user's mental health risk and offers personalized guidance based on their responses. Uses DecisionTreeClassifier

--- 

# Overview
Frontend: Streamlit 

Backend ML: Supervised Machine Learning (Classification)

Model: Decision Tree Classifier

Data: Mental Health in Tech Survey Dataset (Kaggle)

---

# Working 
The application begins by loading a mental health survey dataset containing anonymized responses. Key features such as workplace environment, mental health support, and history are selected

Instead of loading a pre-trained model, this app trains a fresh Decision Tree model every time the app runs

The trained model predicts whether the user is “At Risk” or “Not at Risk” of requiring mental health support

Instead of giving a generic result, the app also analyzes the user’s answers and provides tailored suggestions based on their circumstances — like lack of benefits, remote work isolation, or uncertain support at work

---

# Installations
1. You have to personally download the dataset from Kaggle [https://www.kaggle.com/datasets/osmi/mental-health-in-tech-survey]
2. Clone Repositary :
   git clone https://github.com/paramvarsha12/mental-health-predictor.git
3. To run the application :
   streamlit run main.py



---

# 


