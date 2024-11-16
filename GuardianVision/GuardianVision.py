import streamlit as st 

base="dark"
primaryColor="purple"

# Set the app title 
st.title('GuardianVision') 
# Add a welcome message 
st.write('GuardianVision is an innovative surveillance and monitoring app designed to predict and classify suspicious actions using advanced AI and machine learning. Tailored for security-conscious organizations and businesses, GuardianVision continuously analyzes behaviors, detects anomalies, and generates actionable alerts to help prevent potential threats before they occur. \nWith an intuitive interface, detailed analytics, and seamless integration with your existing security infrastructure, GuardianVision empowers you to maintain safety and control. Built with a focus on accuracy, efficiency, and privacy, GuardianVision is your trusted partner in modern proactive surveillance.') 
# Create a text input 
st.write("Enter your name below:")
name = st.text_input("Your Name")

# Slider
age = st.slider("Select your age:", 0, 100, 25)  # min, max, default

# Button
if st.button("Submit"):
    if name:
        st.success(f"Hello, {name}! You are {age} years old.")
    else:
        st.warning("Please enter your name!")

# Additional content
st.write("This is a simple app to demonstrate Streamlit features.")
