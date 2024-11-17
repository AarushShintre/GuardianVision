import streamlit as st

st.set_page_config(
    page_title="GuardianVision",
    page_icon="🎥",
    layout="centered",
)

# Sidebar Title at the Top
st.sidebar.header("Navigate")

# CSS for Styling Clickable Tabs
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
        }

        .sidebar-tab:hover {
            background-color: #444444;
        }

        .sidebar-tab-selected {
            background-color: #4da6ff;
        }

    </style>
""", unsafe_allow_html=True)

# Function to Display Clickable Tabs and Handle Navigation
def sidebar_tabs(selected_tab):
    tabs = ["File Upload", "Instructions", "About"]
    selected = ""

    for tab in tabs:
        if tab == selected_tab:
            selected = f"<div class='sidebar-tab sidebar-tab-selected'>{tab}</div>"
        else:
            selected = f"<div class='sidebar-tab'>{tab}</div>"

    # Display all tabs
    st.sidebar.markdown(f"""
        <div class="sidebar-tabs">
            {selected}
        </div>
    """, unsafe_allow_html=True)

# Get current selected tab
selected_tab = st.session_state.get('selected_tab', 'File Upload')

# Show tabs in sidebar and allow user to click on them to change the tab
sidebar_tabs(selected_tab)

# Handle tab switching
if selected_tab == "File Upload":
    st.title("🎥 GuardianVision 🎥")
    st.write("Upload an MP4 file to preview it below.")
    
    uploaded_file = st.file_uploader("Choose an MP4 file", type=["mp4"])

    if uploaded_file is not None:
        st.success("File uploaded successfully!")
        st.write("### File Details:")
        st.write(f"**Filename:** {uploaded_file.name}")

        # Display video
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
