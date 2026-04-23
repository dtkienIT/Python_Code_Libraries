import streamlit as st
from helpers.utils import render_video_section, render_docs, render_quiz

TITLE = "Chapter 7: Gradient Descent"
PDF_FOLDER = "data/documents/python_pdf/gradient_descent.pdf"
RADIANT_DESCENT_QUIZ_JSON = "data/questions/radiant_descent_quiz.json"

LESSONS_DATA = {
}

def show():
    # 1. Render Video Section
    render_video_section(title=TITLE, lessons_data=LESSONS_DATA, prefix="rad")
    
    # 2. Render Docs Section
    render_docs(pdf_path=PDF_FOLDER, prefix="rad", title="Tài liệu hướng dẫn Gradient Descent")
    st.write("")
    
    # 3. Render Quiz Section
    render_quiz(quiz_json_path=RADIANT_DESCENT_QUIZ_JSON, course_name="Gradient Descent", prefix="rad")