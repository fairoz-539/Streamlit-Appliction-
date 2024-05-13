import streamlit as st

st.set_page_config(
    page_title="Assignment_writer",
    page_icon="📝",
)

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
