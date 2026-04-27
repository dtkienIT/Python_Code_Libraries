import streamlit as st
from helpers.utils import render_video_section, render_docs, render_quiz

TITLE = "Chapter 12: Support Vector Machine"
PDF_FOLDER = "data/documents/python_pdf/support_vector_machines.pdf"
INTRO_TO_SUPPORT_VECTOR_MACHINE_QUIZ_JSON = "data/questions/support_vector_machine.json"

LESSONS_DATA = {
}

def show():
    # 1. Render Video Section
    render_video_section(title=TITLE, lessons_data=LESSONS_DATA, prefix="svm")
    
    # 2. Render Docs Section
    render_docs(pdf_path=PDF_FOLDER, prefix="svm", title="Tài liệu hướng dẫn Support Vector Machine")
    st.write("")
    
    # 3. Render Quiz Section
    render_quiz(quiz_json_path=INTRO_TO_SUPPORT_VECTOR_MACHINE_QUIZ_JSON, course_name="Introduction to Support Vector Machine", prefix="svm")