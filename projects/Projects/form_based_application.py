from helpers.form_based_helper import *
import streamlit as st

TITLE = "Form-based Application"



def show():
    
    st.title(TITLE)
    
    file_path = "data/documents/excel_files/user_infomation.xlsx"
    
    with st.form("user_form", clear_on_submit=True):
        name = st.text_input("Full Name", key="name")

        birth_date = st.date_input(
            "Date of Birth",
            min_value=datetime(2000, 1, 1),
            max_value=datetime.today()
        )

        email = st.text_input("Email", key="email")

        phone = st.text_input("Phone Number", key="phone")

        job = st.text_input("Occupation", key="job")

        marital_status = st.selectbox(
            "Marital Status",
            ["Single", "Married"]
        )

        is_student = st.checkbox("Are you a student?")

        submit_button = st.form_submit_button("Submit Information")

        if submit_button:
            if not name:
                st.error("Please enter your full name!")
            elif not validate_email(email):
                st.error("Invalid email address!")
            elif not validate_phone(phone):
                st.error("Invalid phone number!")
            else:
                age = calculate_age(birth_date)
                age_status = "Over 18" if age >= 18 else "Under 18"
                status_code = get_status_code(age, job, is_student)
                
                workbook, worksheet = load_existing_excel(file_path)
                worksheet.append([
                    name,
                    birth_date.strftime("%d/%m/%Y"),
                    email,
                    phone,
                    job,
                    marital_status,
                    age_status,
                    status_code
                ])
                
                workbook.save(file_path)
                st.success("Information saved successfully!")
                
    with open(file_path, "rb") as file:
        st.download_button(
            label="📥 Download Excel Report",
            data=file,
            file_name="user_information.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )