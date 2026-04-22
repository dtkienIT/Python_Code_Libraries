import os
import streamlit as st
import mimetypes

# Configuration
TITLE = "Download documents"
SEARCH_LABEL = "🔍 Search by filename..."
DOC_FOLDER = "data/documents/download_sources"

def get_all_files(root_path):
    file_structure = {}
    # Đã bỏ allowed_extensions để cho phép mọi định dạng
    for root, dirs, files in os.walk(root_path):
        # Lọc bỏ các file ẩn của hệ thống (ví dụ: .DS_Store)
        valid_files = [f for f in files if not f.startswith('.')]
        
        if valid_files:
            rel_path = os.path.relpath(root, root_path)
            file_structure[rel_path] = [(f, os.path.join(root, f)) for f in valid_files]
    return file_structure

def get_icon_for_file(filename):
    """Hàm phụ trợ để cấp icon dựa trên đuôi file"""
    ext = filename.lower().split('.')[-1] if '.' in filename else ''
    
    if ext in ['png', 'jpg', 'jpeg', 'gif', 'svg']: return "🖼️"
    if ext in ['zip', 'rar', '7z', 'tar', 'gz']: return "📦"
    if ext in ['py', 'js', 'html', 'css', 'json', 'sql']: return "💻"
    if ext in ['pdf']: return "📕"
    if ext in ['csv', 'xlsx', 'xls']: return "📊"
    if ext in ['doc', 'docx', 'txt', 'md']: return "📝"
    return "📄" # Default cho các file khác

def show():
    # CSS TỐI ƯU: PHÂN BIỆT NÚT SEARCH VÀ NÚT SIDEBAR
    st.markdown("""
        <style>
        /* 2. ĐẢM BẢO NÚT DOWNLOAD VÀ SIDEBAR KHÔNG BỊ ĐỔI MÀU */
        /* Nút Download (secondary) giữ màu trắng xám mặc định */
        div.stButton > button[kind="secondary"] {
            background-color: white !important;
            color: #31333F !important;
            border: 1px solid #d3d3d3 !important;
        }

        /* Nút Sidebar giữ phong cách menu n8n */
        section[data-testid="stSidebar"] div.stButton > button {
            background-color: transparent !important;
            color: #444 !important;
            text-align: left !important;
            border: none !important;
            box-shadow: none !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.title(TITLE)
    st.markdown("---")

    if not os.path.exists(DOC_FOLDER):
        st.error(f"❌ Directory not found: `{DOC_FOLDER}`")
        return

    all_docs = get_all_files(DOC_FOLDER)

    # --- BỐ CỤC PHẦN SEARCH ---
    col_s1, col_s2 = st.columns([0.8, 0.2])
    with col_s1:
        search_query = st.text_input(SEARCH_LABEL, placeholder="Type to filter...").lower()
    with col_s2:
        st.write("<div style='padding-top: 28px;'></div>", unsafe_allow_html=True) 
        # Nút này sẽ nhận màu xanh dương từ CSS vùng Main
        search_button = st.button("Search", use_container_width=True)

    st.divider()
    
    # Logic lọc (giữ nguyên)
    if search_query:
        filtered_docs = {p: [f for f in fs if search_query in f[0].lower()] 
                         for p, fs in all_docs.items()}
        all_docs = {p: fs for p, fs in filtered_docs.items() if fs}

    # Hiển thị kết quả 
    categories = sorted(all_docs.keys())
    root_categories = sorted(list(set([c.split(os.sep)[0] for c in categories])))

    for root_cat in root_categories:
        is_expanded = True if search_query else False
        with st.expander(f"📁 **{root_cat.upper()}**", expanded=is_expanded):
            sub_items = {k: v for k, v in all_docs.items() if k.startswith(root_cat)}
            for path in sorted(sub_items.keys()):
                files = sub_items[path]
                if os.sep in path or "/" in path:
                    st.markdown(f"<div class='lesson-header'>📂 {path.split(os.sep)[-1]}</div>", unsafe_allow_html=True)
                
                for file_name, file_path in files:
                    col1, col2 = st.columns([0.75, 0.25])
                    
                    # Dùng hàm để lấy icon động
                    icon = get_icon_for_file(file_name)
                    
                    with col1:
                        st.markdown(f"<div style='padding:8px 0'><span class='file-text'>{icon} {file_name}</span></div>", unsafe_allow_html=True)
                    with col2:
                        with open(file_path, "rb") as f:
                            st.download_button("Download", f, file_name=file_name, key=file_path, use_container_width=True)