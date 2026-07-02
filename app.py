import streamlit as st
import joblib
scaler = joblib.load("Standarizer.pkl")
model = joblib.load("AdaBoostClassifier.pkl")
st.title("Hello to our classifier")
age = st.number_input("Enter your age: ", min_value=0, max_value=100)
gender = st.radio("Select your gender:", ['Male', 'Female'])
tenure = st.number_input("Enter your tenure: ", min_value=0, max_value=100)
freq = st.number_input("Enter your usage frequency: ", min_value=0, max_value=100)
calls = st.number_input("Enter your support calls: ", min_value=0, max_value=100)
delay = st.number_input("Enter your payment delay: ", min_value=0, max_value=100)
sub_type = st.radio("Select your subscription type:", ['Basic', 'Standard', 'Premium'])
contract_len = st.radio("Select your contract length:", ['Monthly', 'Quarterly', 'Annual'])
total_spend = st.number_input("Enter your total spend: ", min_value=0, max_value=10000)
last_interactoin = st.number_input("Enter your total spend: ", min_value=0, max_value=100)

if st.button("Check Churn!"):
    try:
        gender = 0 if gender == "Male" else 1
        sub_type = 0 if sub_type == "Basic" else 1 if sub_type == "Standard" else 2
        contract_len = 0 if contract_len == "Monthly" else 1 if contract_len == "Quarterly" else 2
        x = [[age, gender, tenure, freq, calls, delay, sub_type, contract_len, total_spend, last_interactoin]]
        x = scaler.transform(x)
        y_pred = model.predict(x)
        st.success("Expecting Churn!" if y_pred[0] == 1 else "Not Expecting Churn!")
    except:
        st.error("Enter valid data")