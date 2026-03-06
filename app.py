import streamlit as st
import importlib
import os

st.set_page_config(page_title="Kien Portfolio", layout="wide")

# Sidebar
st.sidebar.title("Code Library")

DOC_FOLDER = "docs"

pages = {}

# đọc tất cả file python trong docs
for file in os.listdir(DOC_FOLDER):

    if file.endswith(".py"):

        module_name = file.replace(".py","")

        module = importlib.import_module(f"docs.{module_name}")

        # lấy TITLE từ file
        title = getattr(module, "TITLE", module_name)


        pages[f"{title}"] = module_name

# menu sidebar
selected = st.sidebar.radio(
    "Projects",
    list(pages.keys())
)

# load page
module = importlib.import_module(f"docs.{pages[selected]}")

module.show()