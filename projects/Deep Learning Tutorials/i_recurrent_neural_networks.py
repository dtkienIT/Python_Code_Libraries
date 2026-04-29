import streamlit as st
from helpers.utils import render_video_section, render_docs, render_quiz

TITLE = "Chapter 24: Recurrent Neural Networks(RNN)"
PDF_FOLDER = "data/documents/python_pdf/recurrent_neural_networks.pdf"
QUIZ_JSON = "data/questions/recurrent_neural_networks_quiz.json"

LESSONS_DATA = {
}

def show():
    # 1. Render Video Section
    render_video_section(title=TITLE, lessons_data=LESSONS_DATA, prefix="rnn")
    
    # 2. Render Docs Section
    render_docs(pdf_path=PDF_FOLDER, prefix="rnn", title="Tài liệu hướng dẫn Recurrent Neural Networks(RNN)")
    st.write("")
    
    # 3. Render Quiz Section
    render_quiz(quiz_json_path=QUIZ_JSON, course_name="Recurrent Neural Networks(RNN)", prefix="rnn")