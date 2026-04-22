# numpy_course.py
import streamlit as st
from helpers.utils import render_video_section, render_docs, render_quiz

TITLE = "NumPy fundamental course"
PDF_FOLDER = "data/documents/python_pdf/numby.pdf"
NUMPY_QUIZ_JSON = "data/questions/numpy_quiz.json"

LESSONS_DATA = {
    "1. Giới thiệu NumPy": "https://www.youtube.com/watch?v=HxW8EcpWG-Q",
    "2. NumPy Thao Tác Mảng Nâng Cao":"https://www.youtube.com/watch?v=kIKCiT1EEV0&t=212s",
    
}

def show():
    # 1. Render Video Section
    render_video_section(title=TITLE, lessons_data=LESSONS_DATA, prefix="np")
    
    # 2. Render Docs Section
    render_docs(pdf_path=PDF_FOLDER, prefix="np", title="Tài liệu hướng dẫn NumPy")
    st.write("")
    
    # 3. Render Quiz Section
    render_quiz(quiz_json_path=NUMPY_QUIZ_JSON, course_name="NumPy", prefix="np")
