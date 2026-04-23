import streamlit as st
from helpers.utils import render_video_section, render_docs, render_quiz

TITLE = "Chapter 5: Principles of Learning"
PDF_FOLDER = "data/documents/python_pdf/principles_of_learning.pdf"
PRINCIPLES_OF_LEARNING_QUIZ_JSON = "data/questions/principles_of_learning_quiz.json"

LESSONS_DATA = {
}

def show():
    # 1. Render Video Section
    render_video_section(title=TITLE, lessons_data=LESSONS_DATA, prefix="pol")
    
    # 2. Render Docs Section
    render_docs(pdf_path=PDF_FOLDER, prefix="pol", title="Tài liệu hướng dẫn Principles of Learning")
    st.write("")
    
    # 3. Render Quiz Section
    render_quiz(quiz_json_path=PRINCIPLES_OF_LEARNING_QUIZ_JSON, course_name="Principles of Learning", prefix="pol")