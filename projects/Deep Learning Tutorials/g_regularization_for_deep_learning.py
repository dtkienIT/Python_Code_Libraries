import streamlit as st
from helpers.utils import render_video_section, render_docs, render_quiz

TITLE = "Chapter 22: Regularization for Deep Learning"
PDF_FOLDER = "data/documents/python_pdf/regularization_for_deep_learning.pdf"
QUIZ_JSON = "data/questions/regularization_quiz.json"

LESSONS_DATA = {
}

def show():
    # 1. Render Video Section
    render_video_section(title=TITLE, lessons_data=LESSONS_DATA, prefix="rfdl")
    
    # 2. Render Docs Section
    render_docs(pdf_path=PDF_FOLDER, prefix="rfdl", title="Tài liệu hướng dẫn Regularization for Deep Learning")
    st.write("")
    
    # 3. Render Quiz Section
    render_quiz(quiz_json_path=QUIZ_JSON, course_name="Regularization for Deep Learning", prefix="rfdl")