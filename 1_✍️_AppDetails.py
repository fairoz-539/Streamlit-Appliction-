import streamlit as st
from streamlit.errors import StreamlitAPIException

st.set_page_config(
    page_title="Assignment_writer",
    page_icon="🤖",
    layout='wide'
)

def main():
    st.subheader("Welcome To Our App")
    st.write("To Move to our main app click Home and to go to instruction click instructions")
    st.page_link("pages/3_🏠_Home.py",label="Home",icon="🏠")
    st.page_link("pages/2_📑_Home.py",label="Instructions",icon="📑")


if __name__ == '__main__':
    main()

