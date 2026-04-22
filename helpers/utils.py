# utils.py
import streamlit as st
import json
import re
from streamlit_pdf_viewer import pdf_viewer

# --- CÁC HÀM XỬ LÝ DỮ LIỆU ---
@st.cache_data
def load_quiz_data(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

@st.cache_data
def load_pdf(file_path):
    try:
        with open(file_path, "rb") as f:
            return f.read()
    except FileNotFoundError:
        return None

def extract_video_id(url):
    video_id_match = re.search(r"(?<=v=)[^&#]+", url)
    if video_id_match:
        return video_id_match.group(0)
    return None

# --- CÁC HÀM RENDER GIAO DIỆN (UI COMPONENTS) ---

def render_video_section(title, lessons_data, prefix):
    """Render khu vực Header và Video Player dùng chung cho mọi môn học"""
    # --- HEADER ---
    st.title(f"📺 {title}")
    st.markdown("""
    This course is structured for you to add lessons one by one using direct YouTube links.
    Learning source: **Kien Do**.
    """)
    st.markdown("---")

    # --- VIDEO PLAYER SECTION ---
    if not lessons_data:
        st.info("Video bài giảng cho khóa học này đang được cập nhật...")
        st.write("---")
        return

    st.subheader("Select a Lesson")
    # Dùng prefix để key của selectbox không bị trùng giữa các trang
    lesson_name = st.selectbox("Choose a topic to start learning:", list(lessons_data.keys()), key=f"{prefix}_select")

    if lesson_name:
        full_url = lessons_data[lesson_name]
        st.markdown(f"### Currently Watching: {lesson_name}")
        st.video(full_url)
        st.info("🔗 **Original Link:** [Click here to watch on YouTube](https://www.youtube.com/@kiendo729)")
    
    st.write("---")

def render_docs(pdf_path, prefix, title="Tài liệu hướng dẫn"):
    doc_state_key = f"{prefix}_show_docs"
    
    if doc_state_key not in st.session_state:
        st.session_state[doc_state_key] = False

    if not st.session_state[doc_state_key]:
        if st.button("🔽 View docs", key=f"{prefix}_open_docs"):
            st.session_state[doc_state_key] = True
            st.rerun()

    if st.session_state[doc_state_key]:
        with st.container(border=True):
            st.subheader(f"📑 {title}")
            binary_data = load_pdf(pdf_path)
            
            if binary_data:
                pdf_viewer(input=binary_data, width="100%")
            else:
                st.warning("Không tìm thấy file PDF. Vui lòng kiểm tra lại đường dẫn!")
                
            if st.button("🔼 Đóng trang", key=f"{prefix}_close_docs"):
                st.session_state[doc_state_key] = False
                st.rerun()

def render_quiz(quiz_json_path, course_name, prefix):
    q_index_key = f"{prefix}_current_q"
    show_exp_key = f"{prefix}_show_exp"
    
    if q_index_key not in st.session_state:
        st.session_state[q_index_key] = 0
        st.session_state[show_exp_key] = False

    with st.expander(f"📝 Bài tập Trắc nghiệm {course_name}"):
        quiz_data = load_quiz_data(quiz_json_path)
        
        if not quiz_data:
            st.info("Bộ câu hỏi trắc nghiệm đang được cập nhật...")
            return
            
        total_questions = len(quiz_data)
        current_q = st.session_state[q_index_key]
        
        if 0 <= current_q < total_questions:
            item = quiz_data[current_q]
            
            st.write(f"**Tiến độ: {current_q + 1} / {total_questions}**")
            st.progress((current_q + 1) / total_questions)
            
            if "\n\n" in item["question"]:
                question_text, code_text = item["question"].split("\n\n", 1)
                st.subheader(question_text)
                st.code(code_text, language="python")
            else:
                st.subheader(item["question"])
            
            user_choice = st.radio("Chọn đáp án:", options=item["options"], key=f"{prefix}_radio_q_{current_q}")
            
            col1, col2, col3 = st.columns([1, 1, 1])
            with col1:
                if st.button("⬅️ Câu trước", key=f"{prefix}_prev_btn", disabled=(current_q == 0)):
                    st.session_state[q_index_key] -= 1
                    st.session_state[show_exp_key] = False
                    st.rerun()
            with col2:
                if st.button("✅ Xác nhận", key=f"{prefix}_submit_btn"):
                    st.session_state[show_exp_key] = True
            with col3:
                btn_label = "Hoàn thành 🏁" if current_q == total_questions - 1 else "Câu tiếp theo ➡️"
                if st.button(btn_label, key=f"{prefix}_next_btn"):
                    st.session_state[q_index_key] += 1
                    st.session_state[show_exp_key] = False
                    st.rerun()

            if st.session_state[show_exp_key]:
                st.markdown("---")
                if user_choice == item["answer"]:
                    st.success("✅ **Chính xác!**")
                else:
                    st.error(f"❌ **Sai rồi!** Đáp án đúng là: **{item['answer']}**")
                st.info(f"**💡 Giải thích:** {item['explanation']}")
        else:
            st.balloons()
            st.success("🎉 Chúc mừng! Bạn đã hoàn thành bài trắc nghiệm.")
            if st.button("🔄 Làm lại từ đầu", key=f"{prefix}_reset_btn"):
                st.session_state[q_index_key] = 0
                st.session_state[show_exp_key] = False
                st.rerun()