from helpers.cover_letter import CoverLetterProcessor
import streamlit as st

TITLE = "Cover letter"



def show():
    
    st.title(TITLE)
    
    cover_letter_processor = CoverLetterProcessor("data/documents/cover_letters","data/documents/excel_files/so_yeu_ly_lich.xlsx")
    
    
    read_doc = cover_letter_processor.read_docx("data/documents/cover_letters/le_van_c.docx")
    st.write(read_doc)