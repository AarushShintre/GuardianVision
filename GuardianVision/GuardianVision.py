import streamlit as st

st.set_page_config(
    page_title="GuardianVision",
    page_icon="🎥",
    layout="centered",
)

# Sidebar Title at the Top
st.sidebar.header("Navigate")

# CSS for Styling Clickable Rectangles
st.markdown("""
    <style>
        /* Sidebar Styling */
        .sidebar-tabs {
            display: flex;
            flex-direction: column;
            gap: 10px;
        }

        .sidebar-tab {
            padding: 15px;
            background-color: #333333;
            color: #ffffff;
            border-radius: 5px;
            text-align: center;
            cursor: pointer;
            font-size: 16px;
            transition: background-color 0.3s;
            width: 100%;
        }

        .sidebar-tab:hover {
            background-color: #444444;
        }

        .sidebar-tab-selected {
            background-color: #4da6ff;
        }

        .sidebar-tab:active {
            background-color: #005f99;
        }
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
        else:
            st.info("Please upload an MP4 file to continue.")
    
    elif selected_tab == "Instructions":
        st.write(
            """
            ### Upload Instructions:
            1. Click the 'Choose an MP4 file' button to select a file from your computer.
            2. Once the file is uploaded, you will be able to preview it directly in the app.
            3. Supported format: MP4 (up to 200MB).
            """
        )

    elif selected_tab == "About":
        st.write(
            """
            ### About GuardianVision:
            GuardianVision is a video preview tool that allows users to upload MP4 files and 
            view them in a dark-themed interface. Enjoy a seamless video experience!
            """

        )

    elif selected_tab == "Features":
        st.write(
            """
            ### Features of GuardianVision:
            - Easy MP4 file upload and preview.
            - Fast loading of video previews.
            - Simple, intuitive user interface.
            - Dark-themed design for a comfortable viewing experience.
            """
        )

    elif selected_tab == "Contact":
        st.write(
            """
            ### Contact Us:
            If you have any questions or feedback, feel free to reach out to us at:
            - Email: support@guardiavision.com
            - Phone: +1-800-123-4567
            """
        )

    elif selected_tab == "FAQ":
        st.write(
            """
            ### Frequently Asked Questions:
            **Q: What file formats are supported?**  
            A: We currently support MP4 files.

            **Q: How large can my file be?**  
            A: The maximum file size is 200MB.

            **Q: How do I upload my file?**  
            A: Simply click the 'Choose an MP4 file' button and select your file.
            """
        )


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
