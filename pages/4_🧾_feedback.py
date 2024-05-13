import streamlit as st
import os


st.set_page_config(
    page_title="Assignment_writer",
    page_icon="📝",
    layout='wide'
)


# Function to save feedback to a text file
def save_feedback(name, email, feedback):
    feedback_text = f"Name: {name}\nEmail: {email}\nFeedback: {feedback}\n\n"
    with open("feedback.txt", "a") as file:
        file.write(feedback_text)

# Streamlit UI
st.title("Feedback Submission")

# Input fields for name, email, and feedback
name = st.text_input("Enter Your Name:")
email = st.text_input("Enter Your Email:")
feedback = st.text_area("Enter Your Feedback:")

# Submit button
submitted = st.button("Submit")

# Process form submission
if submitted:
    # Check if required fields are filled out
    if not name or not email or not feedback:
        st.error("Please fill out all fields!")
    else:
        # Save feedback to file
        save_feedback(name, email, feedback)
        st.success("Feedback submitted successfully!")
