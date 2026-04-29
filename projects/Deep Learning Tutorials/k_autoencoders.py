import streamlit as st
from helpers.utils import render_video_section, render_docs, render_quiz

TITLE = "Chapter 25: Autoencoders"
PDF_FOLDER = "data/documents/python_pdf/autoencoders.pdf"
QUIZ_JSON = "data/questions/autoencoders_quiz.json"

LESSONS_DATA = {
}

def show():
    # 1. Render Video Section
    render_video_section(title=TITLE, lessons_data=LESSONS_DATA, prefix="ae")
    
    # 2. Render Docs Section
    render_docs(pdf_path=PDF_FOLDER, prefix="ae", title="Tài liệu hướng dẫn Autoencoders")
    st.write("")
    
    # 3. Render Quiz Section
    render_quiz(quiz_json_path=QUIZ_JSON, course_name="Autoencoders", prefix="ae")