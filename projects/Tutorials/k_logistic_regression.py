import streamlit as st
from helpers.utils import render_video_section, render_docs, render_quiz

TITLE = "Chapter 10: Logistic Regression"
PDF_FOLDER = "data/documents/python_pdf/logistic_regression.pdf"
INTRO_TO_LOGISTIC_REGRESSION_QUIZ_JSON = "data/questions/logistic_regression.json"

LESSONS_DATA = {
}

def show():
    # 1. Render Video Section
    render_video_section(title=TITLE, lessons_data=LESSONS_DATA, prefix="log")
    
    # 2. Render Docs Section
    render_docs(pdf_path=PDF_FOLDER, prefix="log", title="Tài liệu hướng dẫn Logistic Regression")
    st.write("")
    
    # 3. Render Quiz Section
    render_quiz(quiz_json_path=INTRO_TO_LOGISTIC_REGRESSION_QUIZ_JSON, course_name="Introduction to Logistic Regression", prefix="log")