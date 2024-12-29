# -*- coding: utf-8 -*-
"""
Created on Fri Dec 13 16:13:10 2024

@author: Nisa
"""

def calculate_credit_score(income, num_houses, num_cars, num_lands, debt, work_years, education, marital_status):
    # Income Level Score
    if income < 10000:
        income_score = 500
    elif 10000 <= income < 20000:
        income_score = 1000
    elif 20000 <= income < 40000:
        income_score = 2000
    elif 40000 <= income < 60000:
        income_score = 3000
    else:
        income_score = 4000
    
    # Number of Houses Score
    house_score = min(num_houses * 100, 300)  # 100 points per house, maximum 300 points

    # Number of Cars Score
    car_score = min(num_cars * 60, 180)  # 60 points per car, maximum 180 points

    # Number of Lands Score
    land_score = min(num_lands * 80, 240)  # 80 points per land, maximum 240 points

    # Debt Situation Score
    if debt == 0:
        debt_score = 2000
    elif debt < 10000:
        debt_score = 1000
    elif 10000 <= debt < 30000:
        debt_score = 500
    else:
        debt_score = 50

    # Work Experience Score
    if work_years <= 5:
        work_score = 500
    elif 6 <= work_years <= 10:
        work_score = 1000
    elif 11 <= work_years <= 20:
        work_score = 2000
    else:
        work_score = 3000

    # Education Level Score
    education_score = {
        "Middle School Graduate": 50,
        "High School Graduate": 100,
        "University": 150,
        "Master's": 200,
        "Doctorate": 250
    }.get

