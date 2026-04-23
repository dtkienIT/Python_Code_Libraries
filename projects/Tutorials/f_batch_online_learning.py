import streamlit as st
from helpers.utils import render_video_section, render_docs, render_quiz

TITLE = "Chapter 6: Batch vs Online Learning"
PDF_FOLDER = "data/documents/python_pdf/batch_online_learning.pdf"
BATCH_VS_ONLINE_LEARNING_QUIZ_JSON = "data/questions/batch_vs_online_learning_quiz.json"

LESSONS_DATA = {
}

def show():
    # 1. Render Video Section
    render_video_section(title=TITLE, lessons_data=LESSONS_DATA, prefix="bol")
    
    # 2. Render Docs Section
    render_docs(pdf_path=PDF_FOLDER, prefix="bol", title="Tài liệu hướng dẫn Batch vs Online Learning")
    st.write("")
    
    # 3. Render Quiz Section
    render_quiz(quiz_json_path=BATCH_VS_ONLINE_LEARNING_QUIZ_JSON, course_name="Batch vs Online Learning", prefix="bol")