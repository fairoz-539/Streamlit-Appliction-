import streamlit as st

st.set_page_config(
    page_title="Assignment Writer",
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

# First page: Introduction
st.header("About Assignment Writer 📝")
st.write("""
Welcome to **Assignment Writer**, your ultimate companion for creating high-quality assignments! 
Our app makes assignment writing more efficient, enjoyable, and stress-free. Generate personalized assignments 
with custom front pages, all while choosing from a variety of font options to suit your unique style.
""")
st.divider()

st.header("Our Mission 🎯")
st.write("""
At Assignment Writer, we empower students to achieve academic excellence. 
We simplify the assignment process, allowing you to focus on learning and personal growth.
""")
st.divider()

# Second page: Features
st.header("App Features 🌟")
st.write("""
**Key Features:**
- 🖥️ **Easy-to-use Interface:** Intuitive design for a seamless experience.
- ✍️ **Customizable Front Page:** Personalize your assignments with essential details.
- 🤖 **AI-Powered Answers:** Generate accurate responses to your questions.
- 🖋️ **Font Selection:** Choose from a variety of fonts to style your assignments.
- 📄 **PDF Generation:** Convert assignments into PDFs with one click.
- 📊 **Progress Bar:** Stay informed with our dynamic progress bar.
- 💬 **Feedback Section:** Share your thoughts and help us improve.
- 🔍 **And much more!**
""")
st.divider()

# Third page: About
st.subheader("Benefits 🎉")
st.write("""
- ⏰ **Time Savings:** Streamline the assignment creation process.
- 📈 **High Quality:** Get reliable and accurate AI-generated answers.
- ⚙️ **Efficiency:** Focus on content without worrying about formatting.
- 🎨 **Customization:** Add a personal touch with custom front pages and fonts.
- 🌐 **Accessibility:** Enjoy a user-friendly interface for all your needs.
- 🤝 **Reliability:** Depend on robust technology for consistent performance.
""")

st.subheader("Our Team 👥")
st.write("""
We're a dedicated team of developers and AI enthusiasts passionate about education and innovation. 
Our goal is to transform learning and empower students worldwide with cutting-edge technology.
""")

st.subheader("Technology Stack 🛠️")
st.write("""
Built with Streamlit, integrating popular data libraries like Pandas, Numpy, and Matplotlib. 
We also use machine learning frameworks like TensorFlow and PyTorch to incorporate AI capabilities.
""")

st.subheader("Future Enhancements 🚀")
st.write("""
We're committed to continuous improvement, adding new features and enhancing functionality. 
Future updates will include more interactive visualizations, additional data sources, and collaborative features.
""")

st.subheader("Support and Feedback 📬")
st.write("""
Have questions or feedback? Reach out through our contact page. 
We value your input and are dedicated to making this app the best it can be. 
Contribute to the project on GitHub by submitting pull requests.
""")

st.subheader("Conclusion 🎓")
st.write("""
Assignment Writer is your trusted partner for academic success. 
Experience the power of AI-assisted learning and let your assignments shine! 💻 ✨
""")
