import streamlit as st
from helpers.utils import render_video_section, render_docs, render_quiz

TITLE = "Chapter 3: Pandas "
PDF_FOLDER = "data/documents/python_pdf/pandas.pdf"
PANDAS_QUIZ_JSON = "data/questions/pandas_quiz.json"

LESSONS_DATA ={
    
}
def show():
    # 1. Render Video Section
    render_video_section(title=TITLE, lessons_data=LESSONS_DATA, prefix="pd")
    
    # 2. Render Docs Section
    render_docs(pdf_path=PDF_FOLDER, prefix="pd", title="Tài liệu hướng dẫn Pandas")
    st.write("")
    
    # 3. Render Quiz Section
    render_quiz(quiz_json_path=PANDAS_QUIZ_JSON, course_name="Pandas", prefix="pd")