import streamlit as st
import subprocess

st.set_page_config(
    page_title="GuardianVision",
    page_icon="🎥",
    layout="centered",
)

# Sidebar Title at the Top
st.sidebar.header("Navigate")

# CSS for Styling
st.markdown("""
    <style>
        /* Add your custom CSS styles here */
    </style>
""", unsafe_allow_html=True)

# Function to display the content of the tabs
def render_tab_content(selected_tab):
    if selected_tab == "File Upload":
        st.title("🎥 GuardianVision 🎥")
        st.write("Upload an MP4 file to preview it below.")
        uploaded_file = st.file_uploader("Choose an MP4 file", type=["mp4"])
        if uploaded_file is not None:
            st.success("File uploaded successfully!")
            st.write("### File Details:")
            st.write(f"**Filename:** {uploaded_file.name}")
            st.video(uploaded_file)

            # Enable the "Train" button only if a file is uploaded
            train_button_enabled = True
        else:
            st.info("Please upload an MP4 file to continue.")
            train_button_enabled = False

        # "Train" Button
        if st.button("Train Model", disabled=not train_button_enabled):
            st.write("Training model... Please wait.")
            try:
                # Call the train_model.py script using subprocess
                result = subprocess.run(
                    ["python", "train_model.py"], capture_output=True, text=True
                )
                if result.returncode == 0:
                    st.success("Model training completed successfully!")
                else:
                    st.error(f"Error during training: {result.stderr}")
            except Exception as e:
                st.error(f"Failed to train the model: {e}")

    elif selected_tab == "Instructions":
        st.write(
            """
            ### Upload Instructions:
            1. Click the 'Choose an MP4 file' button to select a file from your computer.
            2. Once the file is uploaded, you will be able to preview it directly in the app.
            3. Supported format: MP4 (up to 200MB).
            """
        )

    # Add other tabs and content here...

# Create clickable tabs using buttons (styled as rectangles)
tabs = ["File Upload", "Instructions", "About", "Features", "Contact", "FAQ"]
selected_tab = st.session_state.get("selected_tab", "File Upload")

# Display tabs as clickable rectangles
for tab in tabs:
    if st.sidebar.button(tab, key=tab, use_container_width=True):
        selected_tab = tab
        st.session_state.selected_tab = tab

# Render the content of the selected tab
render_tab_content(selected_tab)
