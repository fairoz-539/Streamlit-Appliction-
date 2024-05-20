import streamlit as st
import sqlite3

st.set_page_config(
    page_title="Assignment_writer",
    page_icon="📝",
    layout='wide'
)


hds = """<style>
    #MainMenu {visibility: hidden;}
    footer {visibility : hidden;}
    .main {
     background-image: linear-gradient(to right, #0c1835,#052958);
     opacity: 0.8;
    }
    p,h1{
    font-family:Source Code Pro,monospace;
    }
    
    /* Custom sidebar text color */
    div[data-testid="stSidebarContent"] {
        background-color: #052958; /* Text color */
        font-family: Monospace !important;
    }
    div[data-testid="stSidebarNavSeperator"] {
        background-color: #052958; /* Text color */
    }
    span{
     font-family: Source Code Pro,monospace;
     }
    
    /* Custom input fields color */
    input[type="text"], input[type="number"], input[type="email"], input[type="password"], textarea, select, .st-aw{
        background-color: #0c1835;
        color: #ffffff; /* Text color */
    }

    </style>
"""
st.markdown(hds, unsafe_allow_html=True)


# Function to save feedback to a SQLite3 database
def save_feedback_to_db(name, email, feedback):
    conn = sqlite3.connect("feedback.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS feedback
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, email TEXT, feedback TEXT)''')
    c.execute("INSERT INTO feedback (name, email, feedback) VALUES (?, ?, ?)", (name, email, feedback))
    conn.commit()
    conn.close()

# Function to fetch feedback from the SQLite3 database
def fetch_feedback_from_db():
    conn = sqlite3.connect("feedback.db")
    c = conn.cursor()
    c.execute("SELECT * FROM feedback")
    feedback_data = c.fetchall()
    conn.close()
    return feedback_data

# Streamlit UI
st.title("Feedback Submission")

# Input fields for name, email, and feedback
name = st.text_input("Enter Your Name:")
email = st.text_input("Enter Your Email:")
feedback_text = st.text_area("Enter Your Feedback:")

# Submit button
submitted = st.button("Submit")

# Process form submission
if submitted:
    # Check if required fields are filled out
    if not name or not email or not feedback_text:
        st.error("Please fill out all fields!")
    else:
        # Save feedback to SQLite3 database
        save_feedback_to_db(name, email, feedback_text)
        st.success("Feedback submitted successfully!")


if st.session_state.username == 'frz':
    # Display feedback table
    st.subheader("Feedback Table")
    feedback_data = fetch_feedback_from_db()
    if feedback_data:
        st.write("Here is the list of all feedback received:")
        st.write("|    Name   |    Email    |    Feedback    |")
        st.write("|    ----   |    -----    |    --------    |")
        for row in feedback_data:
            st.write(f"| {row[1]} | {row[2]} | {row[3]} |")
    else:
        st.write("No feedback received yet.")
