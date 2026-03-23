import openpyxl
from datetime import datetime
import re
import pandas as pd
import streamlit as st

def calculate_age(birth_date):
    today = datetime.today()
    age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
    return age

def validate_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

def validate_phone(phone):
    pattern = r'^\d{10,11}$'
    return bool(re.match(pattern, phone))

def get_status_code(age, job, is_student):
    if is_student:
        return 1
    if age >= 18:
        return 3 if job else 2
    return None
def load_existing_excel(file_path):
    """Load existing Excel file or create a new one if it does not exist"""
    try:
        wb = openpyxl.load_workbook(file_path)
        ws = wb["User Information"]
    except FileNotFoundError:
        wb = openpyxl.Workbook()
        ws = wb.active
        ws.title = "User Information"
        headers = [
            "Full Name",
            "Date of Birth",
            "Email",
            "Phone Number",
            "Occupation",
            "Marital Status",
            "Age Status",
            "Status Code"
        ]
        ws.append(headers)
    return wb, ws


def load_data_to_dataframe(file_path):
    """Load data from Excel into a DataFrame for display"""
    try:
        df = pd.read_excel(file_path, sheet_name="User Information")
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=[
            "Full Name",
            "Date of Birth",
            "Email",
            "Phone Number",
            "Occupation",
            "Marital Status",
            "Age Status",
            "Status Code"
        ])
        
