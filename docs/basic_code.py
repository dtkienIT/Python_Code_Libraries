import streamlit as st

TITLE = "Python Basic Example"

def show_block(code):

    # chạy code demo
    exec(code)

    # hiển thị code
    with st.expander("View Code"):
        st.code(code, language="python")
    st.divider()
    
def show():

    st.title(TITLE)

    st.divider()
    code1 = """
st.title("MY PROJECT")
st.header("This is a header")
st.subheader("This is a subheader")
st.caption("This is a caption")
st.text("I love AI VIET NAM")
"""

    show_block(code1)

##############################################################

    code2 = """
st.markdown("Heading 1")
st.markdown("[AI VIET NAM](https://aivietnam.edu.vn/)")
st.markdown(r"$\sqrt{2x+2}$")
st.latex(r"\sqrt{2x+2}")
"""
    show_block(code2)
    
##############################################################

    code3 = """
st.write('I love AI VIET NAM')
st.write('## Heading 2')
st.write(r'$\sqrt{2x+2}$')
st.write('1 + 1 = ', 2)
"""

    show_block(code3)
    
##############################################################
    code4 = """
st.image('data/images/logo.png')
st.image(
    'data/images/dogs.jpeg',
    caption='Funny dogs.'
 )
st.audio('data/audio/audio.mp4')
st.video('data/video/video.mp4')
"""

    show_block(code4)
    
##############################################################
    code5 = """
st.radio(
    "Your favorite color:",
    ['Yellow', 'Bleu'],
    captions = ['Vàng', 'Xanh']
)

option = st.selectbox(
    "Your contact:",
    ("Email", "Home phone", "Mobile phone"))

st.write("Selected:", option)

options = st.multiselect(
    "Your favorite colors:",
    ["Green", "Yellow", "Red", "Blue"],
    ["Yellow", "Red"])

st.write("You selected:", options)

color = st.select_slider(
    "Your favorite color:",
    options=["red", "orange", "violet"])
st.write("My favorite color is", color)
"""
    show_block(code5)
    
##############################################################
    code6 = """
if st.button("Say hello"):
    st.write("Hello")
else:
    st.write("Goodbye")

st.link_button(
    "Go to Google", 
    "https://www.google.com.vn/")
"""
    show_block(code6)
    
##############################################################
    code7 = """
title = st.text_input(
    "Movie title:", "Life of Brian"
)
st.write("The current movie title is", title)
"""
    show_block(code7)

##############################################################
    code8 = """
uploaded_files = st.file_uploader(
    "Choose files", accept_multiple_files=True)
for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)
"""
    show_block(code8)
    
##############################################################
    code9 = """
number = st.number_input("Insert a number")
st.write("The current number is ", number)

values = st.slider(
    "Select a range of values",
    0.0, 100.0, (25.0, 75.0))
st.write("Values:", values)
"""
    show_block(code9)
    
##############################################################
    code10 = """
with st.form("my_form"):
    col1, col2 = st.columns(2)
    f_name = col1.text_input('First Name')
    l_name = col2.text_input('Last Name')
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("First Name: ", f_name, " - Last Name:", l_name)
"""
    show_block(code10)