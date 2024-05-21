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


    # First page: Introduction
st.header(" About Assignment Writer")
st.write("Welcome to Assignment Writer, your ultimate companion for all your assignment needs! Our app is designed to revolutionize the way students tackle their assignments, making the process more efficient, enjoyable, and stress-free. With just a few clicks, you can generate personalized, high-quality assignments with custom front pages, all while exploring a variety of font options to suit your unique style.")
st.divider()
st.write("\n\n\n\n\n")



st.header("Our Mission")
st.write("At Assignment Writer, we strive to empower students to achieve academic excellence. We understand the challenges of managing a heavy workload, tight deadlines, and the pressure to produce high-quality work. That's why we've created this innovative solution to streamline the assignment creation process, ensuring that students can focus on what matters most – their learning and personal growth.")
st.divider()
st.write("\n\n\n\n\n")


# Second page: Features
st.header("App Features")
st.write("This app has several awesome features:")
st.write("- Easy-to-use interface")
st.write("- Interactive data visualization")
st.write("- Machine learning model deployment")
st.write("- User authentication and personalized dashboards")
st.write("- Customizable Front Page: Personalize your assignments with a professional-looking front page that includes all the essential details, such as your name, roll number, section, subject, and assignment number.")
st.write("- Question Answering: Leveraging cutting-edge AI technology, our app generates answers to your questions, providing you with a solid foundation for your assignments.")
st.write("- Font Selection: Choose from a diverse range of font options to add a touch of individuality to your assignments, ensuring they stand out from the crowd.")
st.write("- PDF Generation: Convert your assignments into sleek PDF documents with just one click, making them ready for submission or sharing.")
st.write("- Progress Bar: Stay informed throughout the answer generation process with our dynamic progress bar, providing transparency and peace of mind.")
st.write("- Feedback Section: We value your feedback! Share your thoughts and help us improve the app by navigating to the feedback section in the sidebar. Your input is instrumental in shaping future enhancements.")
st.write("- And much more to come in future updates!")
st.divider()
st.write("\n\n\n\n\n")

    # Third page: About
st.subheader("Benefits")
st.write("- Time Savings: Assignment Writer streamlines the assignment creation process, saving you valuable time and effort.")
st.write("- High Quality: With AI-powered question answering, you can expect accurate and reliable responses, ensuring the quality of your assignments.")
st.write("- Efficiency: Our app eliminates the need for tedious formatting and layout adjustments, allowing you to focus on your ideas and content.")
st.write("- Customization: Personalize your assignments with custom front pages and font selections, making your work truly yours.")
st.write("- Accessibility: Assignment Writer is easily accessible through a user-friendly interface, ensuring a seamless experience for all users.")
st.write("- Reliability: Built with robust technology, our app provides consistent and dependable performance, so you can count on it whenever you need it.")

st.subheader("Our Team")
st.write("Assignment Writer is the brainchild of a dedicated team of developers and AI enthusiasts who share a passion for education and innovation. We believe in the power of technology to transform the way we learn and strive to create tools that empower students to reach their full potential. With a combination of technical expertise and a deep understanding of the challenges faced by students, we've crafted this app to make a real difference in the lives of students worldwide.")

st.subheader("Technology Stack")
st.write("This app is built using Streamlit, which is a Python framework. It integrates seamlessly with popular data libraries such as Pandas, Numpy, and Matplotlib. Additionally, we can leverage machine learning frameworks like TensorFlow and PyTorch to incorporate AI capabilities into our apps.")

st.subheader("Future Enhancements")
st.write("We plan to continuously improve this app by adding more features and enhancing its functionality. This includes integrating more interactive visualizations, supporting additional data sources, and providing collaborative features for teams. We also aim to make the app customizable, allowing users to tailor it to their specific needs.")

st.subheader("Support and Feedback")
st.write("If you have any questions, feedback, or feature requests, please feel free to reach out to us through our contact page. We highly value the input of our users and are committed to making this app the best it can be. You can also contribute to the project by forking the GitHub repository and submitting pull requests.")

st.subheader("Conclusion")
st.write("""Assignment Writer is more than just an app – it's a commitment to supporting students in their academic journey. By leveraging advanced AI technology, we've created a solution that simplifies assignment creation, allowing students to focus on their learning and excel in their studies. We invite you to try Assignment Writer and experience the power of AI-assisted learning. With its intuitive features, customizable options, and reliable performance, it's the ultimate companion for all your assignment needs.

Let Assignment Writer be your trusted partner in the world of academics, empowering you to achieve success and making your assignments truly shine! 💻 📝 🌟

I hope this draft provides a good starting point for your "About Us" section. Feel free to make any changes or additions to ensure it aligns perfectly with your vision and the specifics of your application.""")
