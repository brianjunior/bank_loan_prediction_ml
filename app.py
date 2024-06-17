import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Loan Approvals",
                   layout="wide",
                   page_icon="🧑‍⚕️")

# Loading the saved model
loans_model = pickle.load(open("saved_model.sav", "rb"))

# Sidebar navigation menu
with st.sidebar:
    selected = option_menu('Loan Approval Prediction System',
                           ['Loan Approval', 'See Stats'],
                           icons=['money', 'activity'],
                           default_index=0)

# Loan Approval Prediction
if selected == 'Loan Approval':
    # Page title
    st.title('Bank Loan Approval Prediction Using ML')

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        name = st.text_input('Full Name')
        Gender = st.text_input('Gender (0 for Male, 1 for Female)', '0')
    with col2:
        Married = st.text_input('Married (0 for No, 1 for Yes)', '0')
        Dependents = st.text_input('Dependents (0 for 0, 1 for 1, 2 for 2, 3 for 3+)', '0')
    with col3:
        Education = st.text_input('Education (0 for Not Graduate, 1 for Graduate)', '0')
        Self_Employed = st.text_input('Self Employed (0 for No, 1 for Yes)', '0')
    with col1:
        ApplicantIncome = st.text_input('Applicant Income', '0')
        CoapplicantIncome = st.text_input('Co-Applicant Income', '0')
    with col2:
        LoanAmount = st.text_input('Loan Amount', '0')
        Loan_Amount_Term = st.text_input('Loan Amount Term', '360')
    with col3:
        Credit_History = st.text_input('Credit History (0 for No, 1 for Yes)', '0')
        Property_Area = st.text_input('Property Area (0 for Rural, 1 for Semi, 2 for Urban)', '0')

    # Code for Prediction
    approve_loan = ''

    # Creating a button for Prediction
    if st.button('Loan Approval Prediction'):
        # Prepare the input data for prediction
        try:
            user_input = [
                float(Gender), float(Married), float(Dependents), float(Education), 
                float(Self_Employed), float(ApplicantIncome), float(CoapplicantIncome),
                float(LoanAmount), float(Loan_Amount_Term), float(Credit_History),
                float(Property_Area)
            ]

            # Make prediction
            approve_loan = loans_model.predict([user_input])

            # Display the result with account number and name
            if approve_loan[0] == 1:
                st.success(f"Hello {name}, your loan is approved.")
            else:
                st.error(f"Hello {name}, your loan has been rejected.")
        except ValueError as e:
            st.error(f"Error converting input to numeric: {e}")
