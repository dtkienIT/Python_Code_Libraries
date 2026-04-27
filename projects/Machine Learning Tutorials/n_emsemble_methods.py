import streamlit as st
from helpers.utils import render_video_section, render_docs, render_quiz

TITLE = "Chapter 13: Ensemble Methods"
PDF_FOLDER = "data/documents/python_pdf/ensemble_methods.pdf"
INTRO_TO_ENSEMBLE_METHODS_QUIZ_JSON = "data/questions/ensemble_methods.json"

LESSONS_DATA = {
}

def show():
    # 1. Render Video Section
    render_video_section(title=TITLE, lessons_data=LESSONS_DATA, prefix="em")
    
    # 2. Render Docs Section
    render_docs(pdf_path=PDF_FOLDER, prefix="em", title="Tài liệu hướng dẫn Ensemble Methods")
    st.write("")
    
    # 3. Render Quiz Section
    render_quiz(quiz_json_path=INTRO_TO_ENSEMBLE_METHODS_QUIZ_JSON, course_name="Introduction to Ensemble Methods", prefix="em")