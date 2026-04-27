import streamlit as st
import importlib
import os
import re

st.set_page_config(page_title="Code Library", layout="wide")

# --- CSS TÙY CHỈNH GIAO DIỆN MENU ---
st.markdown("""
    <style>
    /* 1. Xóa bỏ padding mặc định của expander để menu sát lề */
    [data-testid="stExpander"] div[role="vertical"] {
        padding-left: 0.5rem;
    }
    
    /* 2. Style cho các nút bấm giống như đường link menu */
    div.stButton > button {
        border: none;
        background-color: transparent;
        color: #555; /* Màu chữ mặc định */
        text-align: left;
        padding: 5px 10px;
        width: 100%;
        font-size: 15px;
        transition: 0.3s;
    }

    /* 3. Hiệu ứng khi di chuột qua (Hover) */
    div.stButton > button:hover {
        background-color: #f0f2f6; /* Màu nền nhạt khi di chuột */
        color: #ff4b4b !important; /* Màu chữ đổi sang đỏ/cam */
        border-radius: 5px;
    }

    /* 4. Style cho nút đang được chọn (Active) */
    div.stButton > button:active, div.stButton > button:focus {
        color: #ff4b4b !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Header
st.sidebar.title("🚀 Code Library")

DOC_FOLDER = "projects"

# --- CẤU HÌNH THỨ TỰ FOLDER ---
# Định nghĩa thứ tự hiển thị bạn mong muốn tại đây.
# Những folder nào không có tên trong list này sẽ tự động bị đẩy xuống cuối cùng.
CUSTOM_FOLDER_ORDER = [
    "Documentations",
    "Projects",
    "Streamlit Tutorials",
    "Machine Learning Tutorials",
    "Deep Learning Tutorials"
]

# Khởi tạo session_state
if 'current_selection' not in st.session_state:
    st.session_state.current_selection = "-- Welcome Page --"

def get_module_title(file_path):
    """Lấy biến TITLE từ file .py"""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
            match = re.search(r'^TITLE\s*=\s*["\'](.*?)["\']', content, re.MULTILINE)
            if match:
                return match.group(1)
    except:
        pass
    return os.path.basename(file_path).replace(".py", "").replace("_", " ").title()

# --- SIDEBAR MENU ---
if os.path.exists(DOC_FOLDER):
    # 1. Lấy danh sách tất cả các folder thực tế có trong DOC_FOLDER
    actual_folders = [f for f in os.listdir(DOC_FOLDER) if os.path.isdir(os.path.join(DOC_FOLDER, f))]
    
    # 2. Hàm sắp xếp tùy chỉnh
    def sort_folders(folder_name):
        if folder_name in CUSTOM_FOLDER_ORDER:
            return CUSTOM_FOLDER_ORDER.index(folder_name)
        return len(CUSTOM_FOLDER_ORDER) # Đẩy các folder lạ xuống cuối danh sách
        
    # 3. Cập nhật lại list folders theo thứ tự đã định
    folders = sorted(actual_folders, key=sort_folders)
    
    for folder in folders:
        folder_path = os.path.join(DOC_FOLDER, folder)
        
        with st.sidebar.expander(f"📁 {folder}", expanded=False):
            # Các file bên trong folder vẫn được sắp xếp theo bảng chữ cái A-Z
            files = sorted([f for f in os.listdir(folder_path) if f.endswith(".py") and f != "__init__.py"])
            
            for f in files:
                full_path = os.path.join(folder_path, f)
                display_name = get_module_title(full_path)
                
                # Tạo các nút bấm không viền giống như danh sách menu
                if st.button(f"  • {display_name}", key=f"btn_{folder}_{f}"):
                    st.session_state.current_selection = f"projects.{folder}.{f.replace('.py', '')}"
                    st.rerun()

# --- PHẦN HIỂN THỊ MAIN PAGE ---
if st.session_state.current_selection == "-- Welcome Page --":
    st.title("🌟 Welcome to My Page")
    st.markdown("---")
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader("Welcome to the Code Library Repository!")
        st.write("""
            This is a dedicated space for storing and showcasing Python & Streamlit projects.

            **How to use:**
            - Open the folders in the sidebar on the left.
            - Select a document or lesson you wish to view.
            - The content will be automatically loaded onto this page.
        """)
    with col2:
        st.info("💡 **Tip:** To return to this home page, simply reload your browser (F5).")
    st.image("https://images.unsplash.com/photo-1484417894907-623942c8ee29?ixlib=rb-1.2.1&auto=format&fit=crop&w=1350&q=80", use_container_width=True)

else:
    try:
        module_path = st.session_state.current_selection
        module = importlib.import_module(module_path)
        importlib.reload(module)
        module.show()
    except Exception as e:
        st.error(f"❌ Error loading module: {e}")