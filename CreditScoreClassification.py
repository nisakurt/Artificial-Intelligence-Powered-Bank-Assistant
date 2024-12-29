# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18 14:05:28 2024

@author: Nisa
"""

import pandas as pd

# Function to classify creditworthiness based on credit score
def classify_credit_status(score):
    if score <= 699:
        return "Very Risky - Not Eligible for Credit"
    elif 700 <= score <= 1099:
        return "Moderately Risky - Low Limit Credit with Guarantor"
    elif 1100 <= score <= 1499:
        return "Low Risk - Personal Loan (Low-Medium Limit)"
    elif 1500 <= score <= 1699:
        return "Good - Personal and Mortgage Loan (Medium-High Limit)"
    else:  # 1700 - 1900 range
        return "Excellent - Eligible for All Types of Loans"

# Sample DataFrame
data = pd.DataFrame({
    'Credit Score': [1405, 1549, 870, 1170, 1395]
})

# Adding creditworthiness classification to the DataFrame
data['Creditworthiness'] = data['Credit Score'].apply(classify_credit_status)

# Display the table
print(data)

# Function to provide loan recommendations based on credit score, income, and loan type
def loan_recommendation(credit_score, income, loan_type="personal"):
    if credit_score >= 1500:
        if loan_type == "mortgage":
            return "Mortgage Loan - Eligible: Interest Rate 1.2%, Limit: 500,000 TL"
        elif loan_type == "vehicle":
            return "Vehicle Loan - Eligible: Interest Rate 1.5%, Limit: 150,000 TL"
        else:
            return "Personal Loan - Eligible: Interest Rate 1.8%, Limit: 50,000 TL"
    elif 1100 <= credit_score < 1500:
        return "Personal Loan - Low Limit: Interest Rate 2.0%, Limit: 20,000 TL"
    else:
        return "Not eligible for a loan. A higher credit score is required."

# Example usage
print(loan_recommendation(1600, 5000, loan_type="mortgage"))

