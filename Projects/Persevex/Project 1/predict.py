import pickle
import pandas as pd

# Loading the trained pipeline
with open("attrition_pipeline.pkl", "rb") as f:
    pipeline = pickle.load(f)

# Example new employee data
new_employee = pd.DataFrame(
    [
        {
            "Age": 35,
            "BusinessTravel": "Travel_Rarely",
            "Department": "Sales",
            "DistanceFromHome": 10,
            "Education": 3,
            "EducationField": "Life Sciences",
            "EnvironmentSatisfaction": 4,
            "Gender": "Male",
            "JobInvolvement": 3,
            "JobLevel": 2,
            "JobRole": "Sales Executive",
            "JobSatisfaction": 4,
            "MaritalStatus": "Single",
            "MonthlyIncome": 5000,
            "NumCompaniesWorked": 2,
            "OverTime": "Yes",
            "PercentSalaryHike": 15,
            "PerformanceRating": 3,
            "RelationshipSatisfaction": 3,
            "StockOptionLevel": 1,
            "TotalWorkingYears": 10,
            "TrainingTimesLastYear": 2,
            "WorkLifeBalance": 3,
            "YearsAtCompany": 5,
            "YearsInCurrentRole": 3,
            "YearsSinceLastPromotion": 1,
            "YearsWithCurrManager": 3,
        }
    ]
)

try:
    # Predict probability with the model
    risk_score = pipeline.predict_proba(new_employee)[0][1]
    print(f"Attrition Risk Score: {risk_score:.2%}")
    
except ValueError as e:
    print(f"Missing the following values in input:{e}")
