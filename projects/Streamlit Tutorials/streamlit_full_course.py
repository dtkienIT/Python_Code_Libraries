import streamlit as st
import re

# This TITLE variable is used by your main script to display in the sidebar
TITLE = "Python Streamlit Full Course"

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
    Learning source: **Nileg Production**.
    """)
    st.markdown("---")

    # --- LESSON DATA (ADD YOUR LINKS HERE) ---
    # You can now add the full URL for each lesson below
    lessons_data = {
        "1. Streamlit Introduction": "https://www.youtube.com/watch?v=RjiqbTLW9_E&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW&index=1",
        "2. Setting Up the Environment": "https://www.youtube.com/watch?v=6uZYMvsTeBs&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW&index=2",
        "3. Basic Text Elements": "https://www.youtube.com/watch?v=6uZYMvsTeBs&list=PLa6CNrvKM5QU7AjAS90zCMIwi9RTFNIIW&index=3",
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
        st.info(f"🔗 **Original Link:** [Click here to watch on YouTube]({full_url})")

    # --- COURSE OVERVIEW ---
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.write("**Course Details:**")
        st.markdown("- **Platform:** YouTube")
        st.markdown("- **Instructor:** Nileg Production")
    with col2:
        st.write("**Navigation:**")
        st.write("Use the dropdown menu above to switch between lessons.")

    st.divider()
    st.caption("Streamlit Education Series | Learning Repository")

if __name__ == "__main__":
    show()