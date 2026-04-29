import streamlit as st
from helpers.utils import render_video_section, render_docs, render_quiz

TITLE = "Chapter 18: TensorFlow"
PDF_FOLDER = "data/documents/python_pdf/tensorflow.pdf"
QUIZ_JSON = "data/questions/tensorflow_quiz.json"

LESSONS_DATA = {
}

def show():
    # 1. Render Video Section
    render_video_section(title=TITLE, lessons_data=LESSONS_DATA, prefix="tsl")
    
    # 2. Render Docs Section
    render_docs(pdf_path=PDF_FOLDER, prefix="tsl", title="Tài liệu hướng dẫn TensorFlow")
    st.write("")
    
    # 3. Render Quiz Section
    render_quiz(quiz_json_path=QUIZ_JSON, course_name="TensorFlow", prefix="tsl")