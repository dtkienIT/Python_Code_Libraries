import streamlit as st
from helpers.utils import render_video_section, render_docs, render_quiz

TITLE = "Chapter 23: Convolutional Neural Networks(CNN)"
PDF_FOLDER = "data/documents/python_pdf/convolutional_neural_networks.pdf"
QUIZ_JSON = "data/questions/convolutional_neural_networks_quiz.json"

LESSONS_DATA = {
}

def show():
    # 1. Render Video Section
    render_video_section(title=TITLE, lessons_data=LESSONS_DATA, prefix="cnn")
    
    # 2. Render Docs Section
    render_docs(pdf_path=PDF_FOLDER, prefix="cnn", title="Tài liệu hướng dẫn Convolutional Neural Networks(CNN)")
    st.write("")
    
    # 3. Render Quiz Section
    render_quiz(quiz_json_path=QUIZ_JSON, course_name="Convolutional Neural Networks(CNN)", prefix="cnn")