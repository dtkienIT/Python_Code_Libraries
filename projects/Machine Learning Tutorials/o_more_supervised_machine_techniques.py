import streamlit as st
from helpers.utils import render_video_section, render_docs, render_quiz

TITLE = "Chapter 14: More Supervised Machine Learning Techniques"
PDF_FOLDER = "data/documents/python_pdf/more_supervised_machine_techniques.pdf"
QUIZ_JSON = "data/questions/more_supervised_ml_quiz.json"

LESSONS_DATA = {
}

def show():
    # 1. Render Video Section
    render_video_section(title=TITLE, lessons_data=LESSONS_DATA, prefix="msm")
    
    # 2. Render Docs Section
    render_docs(pdf_path=PDF_FOLDER, prefix="msm", title="Tài liệu hướng dẫn More Supervised Machine Learning Techniques")
    st.write("")
    
    # 3. Render Quiz Section
    render_quiz(quiz_json_path=QUIZ_JSON, course_name="More Supervised Machine Learning Techniques", prefix="msm")