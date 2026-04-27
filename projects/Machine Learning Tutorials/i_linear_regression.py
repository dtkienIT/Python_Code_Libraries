import streamlit as st
from helpers.utils import render_video_section, render_docs, render_quiz

TITLE = "Chapter 9: Linear Regression"
PDF_FOLDER = "data/documents/python_pdf/linear_regression.pdf"
INTRO_TO_LINEAR_REGRESSION_QUIZ_JSON = "data/questions/linear_regression.json"

LESSONS_DATA = {
}

def show():
    # 1. Render Video Section
    render_video_section(title=TITLE, lessons_data=LESSONS_DATA, prefix="lg")
    
    # 2. Render Docs Section
    render_docs(pdf_path=PDF_FOLDER, prefix="lg", title="Tài liệu hướng dẫn Linear Regression")
    st.write("")
    
    # 3. Render Quiz Section
    render_quiz(quiz_json_path=INTRO_TO_LINEAR_REGRESSION_QUIZ_JSON, course_name="Introduction to Linear Regression", prefix="lg")