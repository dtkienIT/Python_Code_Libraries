import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import re

TITLE = "Python fundamental course"
PDF_FOLDER = "data/documents/python_pdf/python_basic.pdf"

def extract_video_id(url):
    """
    Helper function to extract the video ID from a standard YouTube URL.
    It works with: 
    - https://www.youtube.com/watch?v=RjiqbTLW9_E
    - https://www.youtube.com/watch?v=RjiqbTLW9_E&list=...&index=1
    """
    video_id_match = re.search(r"(?<=v=)[^&#]+", url)
    if video_id_match:
        return video_id_match.group(0)
    return None

def show():
    
    # --- HEADER ---
    st.title(f"📺 {TITLE}")
    st.markdown("""
    This course is structured for you to add lessons one by one using direct YouTube links.
    Learning source: **Kien Do**.
    """)
    st.markdown("---")

    # --- LESSON DATA (ADD YOUR LINKS HERE) ---
    # You can now add the full URL for each lesson below
    lessons_data = {
        "1. Giới thiệu về Python": "https://www.youtube.com/watch?v=fepWDyU91bo",
        "2. Các Kiểu Dữ Liệu trong Python": "https://www.youtube.com/watch?v=FPVTrlU_-TY&t=14s",
        "3. Biến và Bộ nhớ trong Python": "https://www.youtube.com/watch?v=PZVq8S9yvDo",
        # Add more lessons here following the same format:
        # "Lesson Name": "Full YouTube URL",
    }

    # --- SELECTION UI ---
    st.subheader("Select a Lesson")
    lesson_name = st.selectbox("Choose a topic to start learning:", list(lessons_data.keys()))

    if lesson_name:
        full_url = lessons_data[lesson_name]
        
        # --- VIDEO PLAYER ---
        st.markdown(f"### Currently Watching: {lesson_name}")
        
        # We pass the full URL directly to st.video
        st.video(full_url)
        
        # --- LEARNING NOTES ---
        st.info(f"🔗 **Original Link:** [Click here to watch on YouTube]({"https://www.youtube.com/@kiendo729"})")
    
    with st.expander("View docs"):
        # Đọc file PDF
        with open(PDF_FOLDER, "rb") as f:
            binary_data = f.read()

        # Hiển thị
        pdf_viewer(input=binary_data, width= "100%")