import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the trained model
model = pickle.load(open('saved_model.pkl', 'rb'))

# Sidebar navigation menu
with st.sidebar:
    selected = option_menu('Loan Approval',
                           ['Loan Approval', 'See Stats'],
                           icons=['money', 'activity'],
                           default_index=0)

def run():
    st.title("Bank Loan Prediction using Machine Learning")

    # Input fields in two columns
    col1, col2 = st.columns(2)

    with col1:
        # Account No
        account_no = st.text_input('Account number')

        # Full Name
        fn = st.text_input('Full Name')

        # For gender
        gen_display = ('Female', 'Male')
        gen_options = list(range(len(gen_display)))
        gen = st.selectbox("Gender", gen_options, format_func=lambda x: gen_display[x])

        # For Marital Status
        mar_display = ('No', 'Yes')
        mar_options = list(range(len(mar_display)))
        mar = st.selectbox("Marital Status", mar_options, format_func=lambda x: mar_display[x])

        # No of dependents
        dep_display = ('No', 'One', 'Two', 'More than Two')
        dep_options = list(range(len(dep_display)))
        dep = st.selectbox("Dependents", dep_options, format_func=lambda x: dep_display[x])

        # Applicant Monthly Income
        mon_income = st.number_input("Applicant's Monthly Income($)", value=0)

        # Loan Amount
        loan_amt = st.number_input("Loan Amount", value=0)

    with col2:
        # For education
        edu_display = ('Not Graduate', 'Graduate')
        edu_options = list(range(len(edu_display)))
        edu = st.selectbox("Education", edu_options, format_func=lambda x: edu_display[x])

        # For employment status
        emp_display = ('Job', 'Business')
        emp_options = list(range(len(emp_display)))
        emp = st.selectbox("Employment Status", emp_options, format_func=lambda x: emp_display[x])

        # For Property status
        prop_display = ('Rural', 'Semi-Urban', 'Urban')
        prop_options = list(range(len(prop_display)))
        prop = st.selectbox("Property Area", prop_options, format_func=lambda x: prop_display[x])

        # For Credit Score
        cred_display = ('Between 300 to 500', 'Above 500')
        cred_options = list(range(len(cred_display)))
        cred = st.selectbox("Credit Score", cred_options, format_func=lambda x: cred_display[x])

        # Co-Applicant Monthly Income
        co_mon_income = st.number_input("Co-Applicant's Monthly Income($)", value=0)

        # Loan duration
        dur_display = ['2 Month', '6 Month', '8 Month', '1 Year', '16 Month']
        dur_options = range(len(dur_display))
        dur = st.selectbox("Loan Duration", dur_options, format_func=lambda x: dur_display[x])

    if st.button("Submit"):
        duration = 0
        if dur == 0:
            duration = 60
        elif dur == 1:
            duration = 180
        elif dur == 2:
            duration = 240
        elif dur == 3:
            duration = 360
        elif dur == 4:
            duration = 480

        features = [[gen, mar, dep, edu, emp, mon_income, co_mon_income, loan_amt, duration, cred, prop]]
        
        try:
            prediction = model.predict(features)
            ans = int(prediction[0])
            if ans == 0:
                st.error(
                    f"Hello: {fn} || "
                    f"Account number: {account_no} || "
                    'According to our calculations, you will not get the loan from the bank'
                )
            else:
                st.success(
                    f"Hello: {fn} || "
                    f"Account number: {account_no} || "
                    'Congratulations!! you will get the loan from the bank'
                )
        except Exception as e:
            st.error(f"Error making prediction: {e}")

if selected == 'Loan Approval':
    run()
