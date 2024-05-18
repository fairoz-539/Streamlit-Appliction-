import streamlit as st

st.set_page_config(
    page_title="Assignment_writer",
    page_icon="📝",
)


hds = """<style>
    #MainMenu {}
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


st.title("INSTRUCTIONS !!")


st.info("""\nInstructions to be Followed !
                \nRead the Instructions correctly
                \nStep 1: Enter the Question !
                \nStep 2: Keep the Question clear and concise.
                \nStep 3: Select Font and it\'s color
                \nStep 4: Then click the generate answer button
                \nStep 5: Click View pdf to check Your Generated pdf
                \nStep 6: IF IT\'S OK! Then click download icon from the top right of the viewed pdf""", icon="ℹ️")

st.success("Have Fun Buddy")
st.balloons()
