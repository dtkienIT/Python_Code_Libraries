import streamlit as st
from helpers.utils import render_video_section, render_docs, render_quiz

TITLE = "Chapter 15: Clustering & PCA"
PDF_FOLDER = "data/documents/python_pdf/clustering.pdf"
QUIZ_JSON = "data/questions/clustering_pca_quiz.json"

LESSONS_DATA = {
}

def show():
    # 1. Render Video Section
    render_video_section(title=TITLE, lessons_data=LESSONS_DATA, prefix="cap")
    
    # 2. Render Docs Section
    render_docs(pdf_path=PDF_FOLDER, prefix="cap", title="Tài liệu hướng dẫn Clustering & PCA")
    st.write("")
    
    # 3. Render Quiz Section
    render_quiz(quiz_json_path=QUIZ_JSON, course_name="Clustering & PCA", prefix="cap")