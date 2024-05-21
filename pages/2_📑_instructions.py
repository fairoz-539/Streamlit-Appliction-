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


st.title("My Amazing Streamlit App")

    # First page: Introduction
st.header("Welcome to My App")
st.write("This is a demo app to showcase the use of st.divider and a detailed About page.")
st.write("Let's get started by exploring the different sections below.")
st.divider()

    # Second page: Features
st.header("App Features")
st.write("This app has several awesome features:")
st.write("- Easy-to-use interface")
st.write("- Interactive data visualization")
st.write("- Machine learning model deployment")
st.write("- User authentication and personalized dashboards")
st.write("- And much more to come in future updates!")
st.divider()

    # Third page: About
st.header("About This App")
st.subheader("A Detailed Description")
st.write("This app is designed to showcase the capabilities of Streamlit, a powerful framework for building data-centric web applications. By using Streamlit, we can quickly develop and deploy interactive apps that can handle complex data tasks and provide a user-friendly interface.")

st.subheader("Target Audience")
st.write("This app is targeted towards data scientists, analysts, and developers who want to build and share data apps without spending excessive time on web development. With Streamlit, they can focus on their data-related tasks while still creating beautiful and functional web apps.")

st.subheader("Technology Stack")
st.write("This app is built using Streamlit, which is a Python framework. It integrates seamlessly with popular data libraries such as Pandas, Numpy, and Matplotlib. Additionally, we can leverage machine learning frameworks like TensorFlow and PyTorch to incorporate AI capabilities into our apps.")

st.subheader("Future Enhancements")
st.write("We plan to continuously improve this app by adding more features and enhancing its functionality. This includes integrating more interactive visualizations, supporting additional data sources, and providing collaborative features for teams. We also aim to make the app customizable, allowing users to tailor it to their specific needs.")

st.subheader("Support and Feedback")
st.write("If you have any questions, feedback, or feature requests, please feel free to reach out to us through our contact page. We highly value the input of our users and are committed to making this app the best it can be. You can also contribute to the project by forking the GitHub repository and submitting pull requests.")

st.subheader("Conclusion")
st.write("Thank you for trying out our app. We hope it showcases the potential of Streamlit and inspires you to create your own data-centric web applications. Feel free to explore the app further, and don't hesitate to provide any feedback or suggestions. Happy streaming with Streamlit!")
