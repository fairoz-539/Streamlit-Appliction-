import streamlit as st
from streamlit.errors import StreamlitAPIException

st.set_page_config(
    page_title="Assignment_writer",
    page_icon="🤖",
    layout='wide'
)



# Streamlit UI
st.title("Assignment Writer App")

st.info('Fill this form for Your front page details', icon="ℹ️")
with st.form("form1", clear_on_submit=True, border=True):
    name = st.text_input("Enter Your Name: ")
    rno = st.text_input("Enter Your Roll No: ")
    sec = st.text_input("Enter Your Section: ")
    sub = st.text_input("Enter Your subject title: ")
    assign_num = st.selectbox("Select Assignment number: ", [1, 2])
    btn = st.form_submit_button("Submit")

if btn:
    if not name or not rno or not sub or not assign_num:
        st.error("Please fill out all required fields!")
    else:
        with open("form_values.txt", "w") as file:
            file.write(f"{name}\n")
            file.write(f"{rno}\n")
            file.write(f"{sec}\n")
            file.write(f"{sub}\n")
            file.write(f"{assign_num}\n")
            st.success("Form submitted successfully!")
            st.page_link("pages/3_🏠_Home.py",label="Home")
