import streamlit as st
from streamlit_pdf_viewer import pdf_viewer
import re
import json


TITLE = "Python fundamental course"
PDF_FOLDER = "data/documents/python_pdf/python_basic.pdf"
PYTHON_QUIZ_JSON = "data/questions/python_quiz.json"

# Hàm để đọc dữ liệu từ file JSON
def load_quiz_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return json.load(f)
    
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
        
    with st.expander("Bài tập Trắc nghiệm Python"):
        # 1. Khởi tạo session_state để lưu vị trí câu hỏi hiện tại
        if 'current_question' not in st.session_state:
            st.session_state.current_question = 0
        if 'show_explanation' not in st.session_state:
            st.session_state.show_explanation = False
            
        # Tải dữ liệu
        quiz_data = load_quiz_data(PYTHON_QUIZ_JSON)
        total_questions = len(quiz_data)
        
        # Kiểm tra nếu vẫn còn câu hỏi
        if 0 <= st.session_state.current_question < total_questions:
            i = st.session_state.current_question
            item = quiz_data[i]
            
            # Hiển thị tiến độ và câu hỏi
            st.write(f"**Tiến độ: {i + 1} / {total_questions}**")
            st.progress((i + 1) / total_questions) # Thêm thanh tiến độ cho đẹp
            
            # --- PHẦN MỚI CHỈNH SỬA UI/UX CODE BLOCK ---
            # Kiểm tra xem trong câu hỏi có chứa code không (dựa vào dấu \n\n)
            if "\n\n" in item["question"]:
                question_text, code_text = item["question"].split("\n\n", 1)
                st.subheader(question_text) # In ra câu hỏi
                st.code(code_text, language="python") # Tạo khung đen hiển thị code
            else:
                st.subheader(item["question"]) # Nếu không có code thì in bình thường
            # ---------------------------------------------
            
            # Widget chọn đáp án
            user_choice = st.radio(
                "Chọn đáp án:",
                options=item["options"],
                key=f"q_{i}"
            )
            
            # Chia cột cho các nút điều hướng
            col1, col2, col3 = st.columns([1, 1, 1])
            
            with col1:
                # Nút câu trước
                if st.button("⬅️ Câu trước"):
                    if st.session_state.current_question > 0:
                        st.session_state.current_question -= 1
                        st.session_state.show_explanation = False
                        st.rerun()
                    else:
                        st.warning("Đây là câu hỏi đầu tiên!")

            with col2:
                # Nút xác nhận
                if st.button("✅ Xác nhận"):
                    st.session_state.show_explanation = True

            with col3:
                # Nút câu tiếp theo
                if st.button("Câu tiếp theo ➡️"):
                    if st.session_state.current_question < total_questions - 1:
                        st.session_state.current_question += 1
                        st.session_state.show_explanation = False
                        st.rerun()
                    else:
                        # Nếu là câu cuối cùng, chuyển sang màn hình kết thúc
                        st.session_state.current_question = total_questions
                        st.rerun()

            # Hiển thị kết quả sau khi bấm "Xác nhận"
            if st.session_state.show_explanation:
                if user_choice == item["answer"]:
                    st.success("✅ Chính xác!")
                else:
                    st.error(f"❌ Sai rồi! Đáp án đúng là: {item['answer'][0]}")
                
                st.info(f"**Giải thích:** {item['explanation']}")

        else:
            # Khi đã hết câu hỏi
            st.balloons()
            st.success("🎉 Chúc mừng! Bạn đã hoàn thành bài trắc nghiệm.")
            if st.button("Làm lại từ đầu"):
                st.session_state.current_question = 0
                st.rerun()