import streamlit as st

# Set the page title and layout
st.set_page_config(
    page_title="GuardianVision",
    page_icon="🎥",
    layout="centered",
)

# Add a title and description
st.title("🎥 GuardianVision 🎥")
st.write("Upload an MP4 file to preview it below.")

# Create a file uploader widget
uploaded_file = st.file_uploader("Choose an MP4 file", type=["mp4"])

# Check if a file is uploaded
if uploaded_file is not None:
    st.success("File uploaded successfully!")
    
    # Show file details
    st.write("### File Details:")
    st.write(f"**Filename:** {uploaded_file.name}")
    st.write(f"**File Type:** {uploaded_file.type}")
    st.write(f"**File Size:** {uploaded_file.size / 1024:.2f} KB")
    
    # Display the uploaded video
    st.video(uploaded_file)

else:
    st.info("Please upload an MP4 file to continue.")
