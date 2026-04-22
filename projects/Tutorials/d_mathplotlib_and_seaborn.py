import streamlit as st
from helpers.utils import render_video_section, render_docs, render_quiz

TITLE = "Chapter 4: Mathplotlib and Seaborn"
PDF_FOLDER = "data/documents/python_pdf/mathplotlib_and_seaborn.pdf"
MATHPLOTLIB_SEABORN_QUIZ_JSON = "data/questions/mathplotlib_seaborn_quiz.json"

LESSONS_DATA = {
}

def show():
    # 1. Render Video Section
    render_video_section(title=TITLE, lessons_data=LESSONS_DATA, prefix="mb")
    
    # 2. Render Docs Section
    render_docs(pdf_path=PDF_FOLDER, prefix="mb", title="Tài liệu hướng dẫn Mathplotlib and Seaborn")
    st.write("")
    
    # 3. Render Quiz Section
    render_quiz(quiz_json_path=MATHPLOTLIB_SEABORN_QUIZ_JSON, course_name="Mathplotlib and Seaborn", prefix="mb")