import streamlit as st
from helpers.utils import render_video_section, render_docs, render_quiz

TITLE = "Chapter 11: Regularization for Linear Models"
PDF_FOLDER = "data/documents/python_pdf/regularization_for_linear_models.pdf"
INTRO_TO_REGULARIZATION_FOR_LINEAR_MODELS_QUIZ_JSON = "data/questions/regularization_for_linear_models.json"

LESSONS_DATA = {
}

def show():
    # 1. Render Video Section
    render_video_section(title=TITLE, lessons_data=LESSONS_DATA, prefix="rlm")
    
    # 2. Render Docs Section
    render_docs(pdf_path=PDF_FOLDER, prefix="rlm", title="Tài liệu hướng dẫn Regularization for Linear Models")
    st.write("")
    
    # 3. Render Quiz Section
    render_quiz(quiz_json_path=INTRO_TO_REGULARIZATION_FOR_LINEAR_MODELS_QUIZ_JSON, course_name="Introduction to Regularization for Linear Models", prefix="rlm")