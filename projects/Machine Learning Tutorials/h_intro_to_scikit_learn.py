import streamlit as st
from helpers.utils import render_video_section, render_docs, render_quiz

TITLE = "Chapter 8: Introduction to Scikit-learn"
PDF_FOLDER = "data/documents/python_pdf/introduction_to_scikit_learn.pdf"
INTRO_TO_SCIKIT_LEARN_QUIZ_JSON = "data/questions/introduction_to_scikit_learn.json"

LESSONS_DATA = {
}

def show():
    # 1. Render Video Section
    render_video_section(title=TITLE, lessons_data=LESSONS_DATA, prefix="isk")
    
    # 2. Render Docs Section
    render_docs(pdf_path=PDF_FOLDER, prefix="isk", title="Tài liệu hướng dẫn Introduction to Scikit-learn")
    st.write("")
    
    # 3. Render Quiz Section
    render_quiz(quiz_json_path=INTRO_TO_SCIKIT_LEARN_QUIZ_JSON, course_name="Introduction to Scikit-learn", prefix="isk")