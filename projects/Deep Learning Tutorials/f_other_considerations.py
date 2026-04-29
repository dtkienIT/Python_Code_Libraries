import streamlit as st
from helpers.utils import render_video_section, render_docs, render_quiz

TITLE = "Chapter 21: Other Considerations in Deep Learning"
PDF_FOLDER = "data/documents/python_pdf/other_considerations.pdf"
QUIZ_JSON = "data/questions/other_considerations_quiz.json"

LESSONS_DATA = {
}

def show():
    # 1. Render Video Section
    render_video_section(title=TITLE, lessons_data=LESSONS_DATA, prefix="orc")
    
    # 2. Render Docs Section
    render_docs(pdf_path=PDF_FOLDER, prefix="orc", title="Tài liệu hướng dẫn Other Considerations in Deep Learning")
    st.write("")
    
    # 3. Render Quiz Section
    render_quiz(quiz_json_path=QUIZ_JSON, course_name="Other Considerations in Deep Learning", prefix="orc")