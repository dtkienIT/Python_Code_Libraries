import streamlit as st
from helpers.utils import render_video_section, render_docs, render_quiz

TITLE = "Chapter 1: Python"
PDF_FOLDER = "data/documents/python_pdf/python_basic.pdf"
PYTHON_QUIZ_JSON = "data/questions/python_quiz.json"

LESSONS_DATA = {
    "1. Giới thiệu về Python": "https://www.youtube.com/watch?v=fepWDyU91bo",
    "2. Các Kiểu Dữ Liệu trong Python": "https://www.youtube.com/watch?v=FPVTrlU_-TY&t=14s",
    "3. Biến và Bộ nhớ trong Python": "https://www.youtube.com/watch?v=PZVq8S9yvDo",
    "4. Top 3 của Python List, Tuple, & Dictionary":"https://www.youtube.com/watch?v=DCbJSQ8HsY0",
    "5. Làm Chủ List trong Python": "https://www.youtube.com/watch?v=E-jtsAn-MPo",
    "6. Làm chủ String trong Python":"https://www.youtube.com/watch?v=w810cbqdC5k",
    "7. Giải mã Python Các toán tử cốt lõi":"https://www.youtube.com/watch?v=VKwV2BfNqhw",
    "8. Để mã Python của bạn cất lời":"https://www.youtube.com/watch?v=RsIbrLHoSR8&t=73s",
    "9. Python Câu lệnh Điều kiện và Vòng lặp": "https://www.youtube.com/watch?v=cs-OtJlrk1o",
    "10. Nâng Cấp Python Của Bạn":"https://www.youtube.com/watch?v=atExoMjddHY"
}

def show():
    # 1. Render Video Section
    render_video_section(title=TITLE, lessons_data=LESSONS_DATA, prefix="py")
    
    # 2. Render Docs Section
    render_docs(pdf_path=PDF_FOLDER, prefix="py", title="Tài liệu hướng dẫn Python")
    st.write("")
    
    # 3. Render Quiz Section
    render_quiz(quiz_json_path=PYTHON_QUIZ_JSON, course_name="Python", prefix="py")
