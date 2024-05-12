import streamlit as st
from streamlit.errors import StreamlitAPIException

st.set_page_config(
    page_title="Assignment_writer",
    page_icon="🤖",
    layout='wide'
)

st.pagelink("3_🏠_Home.py",icon="🏠")
st.write("# Assignment Writer App 🤖

Welcome to the Assignment Writer App! This app allows you to generate digital assignments quickly and easily.

## Features

✏️ Generate assignments with ease  
🔍 Get answers from Wikipedia  
📄 Download assignments as PDF  

## Installation

To install the Assignment Writer App, follow these steps:

1. Clone this repository to your local machine.
2. Install the required dependencies by running: `pip install -r requirements.txt`.
3. Run the app using Streamlit: `streamlit run app.py`.

## Usage

1. Enter your question in the input box provided.
2. Click on the "Generate Answer" button to get the answer from Wikipedia.
3. Customize the font and colors using the dropdown menus.
4. Click on the "Generate PDF" button to download the assignment as a PDF.

## Themes

The app supports the following themes:

- Base: Dark
- Primary Color: #3744f7
- Background Color: #0c1835
- Secondary Background Color: #052958
- Font: Monospace

## Feedback

We're constantly improving the Assignment Writer App. If you have any feedback or suggestions, please feel free to [submit an issue]or [reach out to us].

## Contributors

- Fairoz (Salroz)

")


