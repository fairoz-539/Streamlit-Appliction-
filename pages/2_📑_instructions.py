import streamlit as st

st.set_page_config(
    page_title="Assignment_writer",
    page_icon="🤖"
)

st.title("INSTRUCTIONS !!")


st.info("""\nInstructions to be Followed !\n
                Read the Instructions correctly\n 
                Step 1: Enter the Question !\n
                Step 2:Keep the Question clear and concise.\n
                Step 3: Select Font and it\'s color\n
                Step 4: Then click the generate answer button\n
                Step 5: Click View pdf to check Your Generated pdf\n
                Step 6: IF IT\'S OK! Then click download icon from the top right of the viewed pdf\n""", icon="ℹ️")

st.success("Have Fun Buddy")
st.balloons()
