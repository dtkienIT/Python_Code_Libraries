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
"""