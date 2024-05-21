import streamlit as st
import cohere
import sqlite3
import os
import time
import wikipedia as wk
from xhtml2pdf import pisa
import base64
from streamlit.errors import StreamlitAPIException

# Set up page configuration
st.set_page_config(
    page_title="Assignment Writer",
    page_icon="📝",
    layout='wide',
    initial_sidebar_state="collapsed"
)

api_key = st.secrets["cohere"]["api_key"]

# Initialize Cohere client
co = cohere.Client(api_key=api_key)

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
    input[type="text"], input[type="number"], input[type="email"], input[type="password"], textarea, select, .st-aw{
        background-color: #0c1835;
        color: #ffffff; /* Text color */
    }
    </style>
"""
st.markdown(hds, unsafe_allow_html=True)




# Create profile pictures directory if it doesn't exist
if not os.path.exists("profile_pics"):
    os.makedirs("profile_pics")

# Function to create users table
def create_user_table():
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT UNIQUE, password TEXT, profile_pic TEXT)''')
    conn.commit()
    conn.close()

# Function to add a user to the database
def add_user(username, password, profile_pic):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("INSERT INTO users (username, password, profile_pic) VALUES (?, ?, ?)", (username, password, profile_pic))
    conn.commit()
    conn.close()

# Function to validate a user
def validate_user(username, password):
    conn = sqlite3.connect("users.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    user = c.fetchone()
    conn.close()
    return user

# Function to save feedback to SQLite3 database
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


def generate_answer(question):
    try:
        if question:
            stream = co.chat_stream(message=question)
            answer = ""
            for event in stream:
                if event.event_type == "text-generation":
                    answer += event.text
        else:
            st.warning("Please enter a question.")
        return answer
    except Exception as e:
        st.error("Error generating answer: {}".format(e))


def generate_pdf(question, answer, name, rno, sec, sub, assign_num, font_family="Source Code Pro,monospace"):
    try:
        # Create a PDF document
        pdf_data = f"""
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Assignment</title>
            <style>
                body {{
                    font-family: 'Times New Roman', Times, serif;
                    margin: 0;
                    padding: 0;
                    counter-reset: page;
                    pdf-outline: true;
                }}
                .header {{
                    text-align: center;
                    padding: 20px;
                    padding-top: 200px;
                    font-size: 30px;
                }}
                .assignment-info {{
                    margin: 20px auto;
                    display: inline-block;
                    text-align: left;
                }}
                .assignment-info table {{
                    border-collapse: collapse;
                    width: 100%;
                }}
                .assignment-info th, .assignment-info td {{
                    border: 1px solid black;
                    padding: 10px;
                    text-align: center;
                }}
                .page-number::after {{
                    counter-increment: page;
                    content: counter(page);
                }}
                .assignment-start {{
                    text-align: left;
                    page-break-before: always;
                    padding: 20px;
                    font-size: 20px;
                }}
                .assignment-title {{
                    text-align: center;
                    font-size: 24px;
                    font-weight: bold;
                    margin-bottom: 20px;
                }}
            </style>
        </head>
        <body>
            <pdf:toc />
            <div class="header">
                <div class="assignment-info">
                    <h1 style="text-align: center">Assignment Details</h1>
                    <table>
                        <tr>
                            <th>Subject Title</th>
                            <td>{sub}</td>
                        </tr>
                        <tr>
                            <th>Assignment</th>
                            <td>{assign_num}</td>
                        </tr>
                        <tr>
                            <th>Name</th>
                            <td>{name}</td>
                        </tr>
                        <tr>
                            <th>Roll No</th>
                            <td>{rno}</td>
                        </tr>
                        <tr>
                            <th>Section</th>
                            <td>{sec}</td>
                        </tr>
                    </table>
                </div>
            </div>
            <div class="assignment-start">
                <p style="padding-top: 80px;text-align:center;font-size:28px;font-family:{font_family}"><strong>{question}</strong></p>
                <p style="font-family:{font_family};">{answer}</p>
            </div>
        </body>
        </html>
        """

        # Generate PDF from HTML
        pdf_file_path = "output.pdf"
        with open(pdf_file_path, "wb") as f:
            pisa_status = pisa.CreatePDF(pdf_data, dest=f)
            if pisa_status.err:
                raise Exception("Error generating PDF")

        return pdf_file_path
    except Exception as e:
        raise e
    

# Main app function
def main_app():
    # st.title("Assignment Writer App")
    st.sidebar.info('Fill this form for Your front page details', icon="ℹ️")
    with st.sidebar.form("form1", clear_on_submit=True, border=True):
        name = st.text_input("Enter Your Name: ")
        rno = st.text_input("Enter Your Roll No: ")
        sec = st.text_input("Enter Your Section: ")
        sub = st.text_input("Enter Your subject title: ")
        assign_num = st.selectbox("Select Assignment number: ", [1, 2])
        btn = st.form_submit_button("Submit")

    if btn:
        if not name or not rno or not sub or not assign_num:
            st.sidebar.error("Please fill out all required fields!")
        else:
            with open("form_values.txt", "w") as file:
                st.sidebar.success("Form submitted successfully!")
    st.subheader(f"Welcome, {st.session_state['username']}")
    st.write("\n\n\n\n\n\n\n\n\n")
    st.warning("Please fill the front details if not filled. Navigate to sidebar and fill the form.",icon="ℹ️")


    if "question" not in st.session_state:
        st.session_state.question = ""
    if "font_family" not in st.session_state:
        st.session_state.font_family = 'Source Code Pro,monospace'
    if "Gen_Ans" not in st.session_state:
        st.session_state.Gen_Ans = False
    if "Gen_PDF" not in st.session_state:
        st.session_state.Gen_PDF = False
    if "Answer" not in st.session_state:
        st.session_state.Answer = None

    st.write("\n\n\n\n\n\n\n\n\n\n\n")
    # Get user input
    st.session_state.question = st.text_input("Enter Your Question:", value=st.session_state.question)
            
    # Select custom font
    font_options = [
        'Source Code Pro,monospace','Arial', 'Times New Roman', 'Courier New', 'Verdana',
        'Helvetica', 'Georgia', 'Comic Sans MS', 'Impact', 'Tahoma',
        'Brush Script MT', 'Lucida Handwriting', 'Papyrus', 'Segoe Script'
        # Add more fonts as needed
    ]
    st.write("\n\n\n\n\n\n\n\n\n")
    st.session_state.font_family = st.selectbox("Select Font Family:", font_options, index=font_options.index(st.session_state.font_family), disabled=True)
    
    # Button to generate the answer
    st.write("\n\n\n\n\n\n\n\n")
    gen_answer = st.button("Generate Answer")

    # Generate answer when the button is clicked
    if gen_answer:
        st.session_state.Gen_Ans = True
        st.session_state.Gen_PDF = False  # Reset the PDF generation state
        # Add a placeholder
        st.write("\n\n\n\n\n\n\n\n")
        latest_iteration = st.empty()
        bar = st.progress(0)

        for i in range(100):
            # Update the progress bar with each iteration.
            latest_iteration.text(f'Loading ....')
            bar.progress(i + 1)
            time.sleep(0.1)
        st.write("\n\n\n\n\n\n\n\n")
        st.session_state.Answer = generate_answer(st.session_state.question)
        latest_iteration.text(f'Loading Complete')

    if st.session_state.Gen_Ans and st.session_state.Answer:
        answer = st.session_state.Answer

        # with col3:
        #     st.title(st.session_state.question)
        #     st.write(answer)
            # Display answer in HTML format
        st.markdown(
                # f"<h1 style='font-family:{st.session_state.font_family};'>{st.session_state.question}</h1>
                f"<span style='font-family:{st.session_state.font_family}'>{answer}</span>",
                unsafe_allow_html=True)
        st.balloons()

        st.write("\n\n\n\n\n\n")
        gen_pdf = st.button("Generate PDF")

        if gen_pdf:
            st.session_state.Gen_PDF = True

    if st.session_state.Gen_PDF:
        latest_iteration = st.empty()
        bar = st.progress(0)
        for i in range(100):
            # Update the progress bar with each iteration.
            latest_iteration.text(f'Generating PDF ....')
            bar.progress(i + 1)
            time.sleep(0.2)
        latest_iteration.text(f'Done')

        answer = st.session_state.Answer
        if answer:
            try:
                pdf_file_path = generate_pdf(st.session_state.question, answer, name, rno, sec, sub, assign_num, st.session_state.font_family)
                if pdf_file_path:
                    st.success("PDF generated successfully!")
                    with open(pdf_file_path, "rb") as f:
                        pdf_contents = f.read()
                        base64_pdf = base64.b64encode(pdf_contents).decode("utf-8")
                        # Display download link
                        download_link = f'<a href="data:application/pdf;base64,{base64_pdf}" download="Output.pdf">Download PDF</a>'
                        st.markdown(download_link, unsafe_allow_html=True)
                        st.balloons()
            except Exception as e:
                st.error("Error generating PDF: {}".format(e))
        else:
            st.error("Error generating PDF.")

    st.write("\n\n\n\n\n")
    st.write("To Give feedback click the below option !")
    st.page_link("pages/4_🧾_feedback.py", label="Give Feedback", icon="🧾")
    st.write("\n\n\n\n\n\n\n\n\n")
    st.info("""Our application is still in training phase, so it may encounter occasional errors or inaccuracies.
        We value your feedback to help improve and refine its performance. Please take a moment to share your thoughts by navigating to the feedback section in the sidebar. Your input is greatly appreciated!""")
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #052958;
            color: white;
            text-align: center;
            padding: 10px 0;
            font-family: Arial, sans-serif;
        }
        </style>
        """, unsafe_allow_html=True
    )
    st.markdown('<div class="footer">Digital Assignmennt Writer App - frz</div>', unsafe_allow_html=True)
# Main function
def main():
    create_user_table()

    # st.title("Assignment writer")
    st.markdown(
        '<div class="container"><div class="typed-out">ASSIGNMENT WRITER</div></div>',
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <style>
        .container {
            display: inline-block;
        }
        .typed-out {
            overflow: hidden;
            border-right: 0.15em solid orange;
            white-space: nowrap;
            animation: typing 5s steps(12, end) forwards infinite;
            font-size: 1.6rem;
            width: 0;
        }
        @keyframes typing {
            from { width: 0 }
            to { width: 100% }
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if st.session_state.logged_in:
        main_app()
        if st.sidebar.button("Logout"):
            st.session_state.logged_in = False
            st.session_state.username = None
            st.session_state.profile_pic = None
            st.success("You have been logged out.")
        else:
            st.sidebar.write(f"Usename: {st.session_state['username']}")
            if st.session_state.profile_pic:
                st.sidebar.image(st.session_state.profile_pic, width=100)
            
    else:
        menu = ["Login", "Sign Up"]
        choice = st.selectbox("Menu", menu)

        if choice == "Login":
            st.subheader("Login Section")
            username = st.text_input("Username")
            password = st.text_input("Password", type='password')
            if st.button("Login"):
                user = validate_user(username, password)
                if user:
                    st.session_state.logged_in = True
                    st.session_state.username = username
                    st.session_state.profile_pic = user[3]

                    # Show loader
                    loader_html = """
                    <style>
                    .loader-container {
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        position: fixed;
                        left: 0;
                        top: 0;
                        width: 100%;
                        height: 100%;
                        background-color: black;
                        z-index: 1000;
                    }
                    .loader {
                        font-size: 100px;
                        animation: zoomInOut 1s infinite;
                    }
                    @keyframes zoomInOut {
                        0% { transform: scale(1); }
                        50% { transform: scale(1.2); }
                        100% { transform: scale(1); }
                    }
                    @keyframes changeColor {
                        0% { color: #007bff; }
                        25% { color: #28a745; }
                        50% { color: #dc3545; }
                        75% { color: #ffc107; }
                        100% { color: #007bff; }
                    }
                    @keyframes changeText {
                        0%, 35% { content: 'F'; }
                        35%, 50% { content: 'R'; }
                        50%, 60% { content: 'Z'; }
                        60%, 100% { content: 'Frz'; }
                    }
                    .loader::before {
                        content: 'F';
                        animation: changeText 8s infinite, changeColor 8s infinite;
                    }
                    </style>
                    <div class="loader-container">
                        <div class="loader"></div>
                    </div>
                    <script>
                    setTimeout(function() {
                        document.querySelector('.loader-container').style.display = 'none';
                    }, 10000);
                    </script>
                    """
                    st.markdown(loader_html, unsafe_allow_html=True)
                    time.sleep(10)
                    st.experimental_rerun()
                else:
                    st.error("Invalid Username or Password")

        elif choice == "Sign Up":
            st.subheader("Create New Account")
            new_user = st.text_input("Username")
            new_password = st.text_input("Password", type='password')
            profile_pic = st.file_uploader("Upload Profile Picture", type=["png", "jpg", "jpeg"])

            if st.button("Sign Up"):
                if profile_pic is not None:
                    profile_pic_path = os.path.join("profile_pics", new_user + "_" + profile_pic.name)
                    with open(profile_pic_path, "wb") as f:
                        f.write(profile_pic.getbuffer())
                else:
                    profile_pic_path = None

                try:
                    add_user(new_user, new_password, profile_pic_path)
                    st.success("Account created successfully")
                    st.info("Go to Login Menu to login")
                except sqlite3.IntegrityError:
                    st.error("Username already exists")

  
    st.markdown(
        """
        <style>
        .footer {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            background-color: #052958;
            color: white;
            text-align: center;
            padding: 10px 0;
            font-family: Arial, sans-serif;
        }
        </style>
        """, unsafe_allow_html=True
    )
    st.markdown('<div class="footer">Digital Assignmennt Writer App - frz</div>', unsafe_allow_html=True)
if __name__ == '__main__':
    main()







# # import streamlit as st
# # import wikipedia as wk
# # from xhtml2pdf import pisa
# # import base64
# # from streamlit.errors import StreamlitAPIException
# # import time

# # st.set_page_config(
# #     page_title="frz_Assignment_writer App",
# #     page_icon="📝",
# #     layout='wide',
# #     initial_sidebar_state="expanded",
# # )

# # hds = """<style>
# #     #MainMenu {}
# #     footer {visibility : hidden;}
# #     .main {
# #      background-image: linear-gradient(to right, #0c1835,#052958);
# #      opacity: 0.8;
# #     }
# #     p,h1{
# #     font-family:Source Code Pro,monospace;
# #     }
    
# #     /* Custom sidebar text color */
# #     div[data-testid="stSidebarContent"] {
# #         background-color: #052958; /* Text color */
# #         font-family: Monospace !important;
# #     }
# #     div[data-testid="stSidebarNavSeperator"] {
# #         background-color: #052958; /* Text color */
# #     }
# #     span{
# #      font-family: Source Code Pro,monospace;
# #      }
    
# #     /* Custom input fields color */
# #     input[type="text"], input[type="number"], input[type="email"], input[type="password"], textarea, select, .st-aw{
# #         background-color: #0c1835;
# #         color: #ffffff; /* Text color */
# #     }

# #     </style>
# # """
# # st.markdown(hds, unsafe_allow_html=True)

# # def generate_answer(question):
# #     try:
# #         # Get answer from Wikipedia
# #         answer = wk.summary(question)
# #         return answer
# #     except wk.exceptions.DisambiguationError as e:
# #         return st.error("Error generating answer: {}".format(e))
# #     except wk.exceptions.PageError as e:
# #         return st.error("Error generating answer: {}".format(e))
# #     except wk.exceptions.WikipediaException:
# #         st.warning("Error generating answer: Wikipedia search parameter is not set. No match for an empty query.")
# #     except Exception as e:
# #         return st.error("Error generating answer: {}".format(e))

# # def generate_pdf(question, answer, name, rno, sec, sub, assign_num, font_family="Arial", heading_color="#393b3d", text_color="#307bd1"):
# #     try:
# #         # Create a PDF document
# #         pdf_data = f"""
# #         <html lang="en">
# #         <head>
# #             <meta charset="UTF-8">
# #             <meta name="viewport" content="width=device-width, initial-scale=1.0">
# #             <title>Assignment</title>
# #             <style>
# #                 body {{
# #                     font-family: 'Times New Roman', Times, serif;
# #                     margin: 0;
# #                     padding: 0;
# #                     counter-reset: page;
# #                     pdf-outline: true;
# #                 }}
# #                 .header {{
# #                     text-align: center;
# #                     padding: 20px;
# #                     padding-top: 200px;
# #                     font-size: 30px;
# #                 }}
# #                 .assignment-info {{
# #                     margin: 20px auto;
# #                     display: inline-block;
# #                     text-align: left;
# #                 }}
# #                 .assignment-info table {{
# #                     border-collapse: collapse;
# #                     width: 100%;
# #                 }}
# #                 .assignment-info th, .assignment-info td {{
# #                     border: 1px solid black;
# #                     padding: 10px;
# #                     text-align: center;
# #                 }}
# #                 .page-number::after {{
# #                     counter-increment: page;
# #                     content: counter(page);
# #                 }}
# #                 .assignment-start {{
# #                     text-align: left;
# #                     page-break-before: always;
# #                     padding: 20px;
# #                     font-size: 20px;
# #                 }}
# #                 .assignment-title {{
# #                     text-align: center;
# #                     font-size: 24px;
# #                     font-weight: bold;
# #                     margin-bottom: 20px;
# #                 }}
# #             </style>
# #         </head>
# #         <body>
# #             <pdf:toc />
# #             <div class="header">
# #                 <div class="assignment-info">
# #                     <h1 style="text-align: center">Assignment Details</h1>
# #                     <table>
# #                         <tr>
# #                             <th>Subject Title</th>
# #                             <td>{sub}</td>
# #                         </tr>
# #                         <tr>
# #                             <th>Assignment</th>
# #                             <td>{assign_num}</td>
# #                         </tr>
# #                         <tr>
# #                             <th>Name</th>
# #                             <td>{name}</td>
# #                         </tr>
# #                         <tr>
# #                             <th>Roll No</th>
# #                             <td>{rno}</td>
# #                         </tr>
# #                         <tr>
# #                             <th>Section</th>
# #                             <td>{sec}</td>
# #                         </tr>
# #                     </table>
# #                 </div>
# #             </div>
# #             <div class="assignment-start">
# #                 <p style="padding-top: 80px;text-align:center;font-size:28px;"><strong>{question}</strong></p>
# #                 <p>{answer}</p>
# #             </div>
# #         </body>
# #         </html>
# #         """

# #         # Generate PDF from HTML
# #         pdf_file_path = "output.pdf"
# #         with open(pdf_file_path, "wb") as f:
# #             pisa_status = pisa.CreatePDF(pdf_data, dest=f)
# #             if pisa_status.err:
# #                 raise Exception("Error generating PDF")

# #         return pdf_file_path
# #     except Exception as e:
# #         raise e

# # st.title("Assignment Writer App")
# # st.sidebar.info('Fill this form for Your front page details', icon="ℹ️")
# # with st.sidebar.form("form1", clear_on_submit=True, border=True):
# #     name = st.text_input("Enter Your Name: ")
# #     rno = st.text_input("Enter Your Roll No: ")
# #     sec = st.text_input("Enter Your Section: ")
# #     sub = st.text_input("Enter Your subject title: ")
# #     assign_num = st.selectbox("Select Assignment number: ", [1, 2])
# #     btn = st.form_submit_button("Submit")

# # if btn:
# #     if not name or not rno or not sub or not assign_num:
# #         st.sidebar.error("Please fill out all required fields!")
# #     else:
# #         with open("form_values.txt", "w") as file:
# #             st.sidebar.success("Form submitted successfully!")
# # st.warning("Please fill the front details if not filled. Navigate to sidebar and fill the form.",icon="ℹ️")


# # if "question" not in st.session_state:
# #     st.session_state.question = ""
# # if "font_family" not in st.session_state:
# #     st.session_state.font_family = 'Arial'
# # if "Gen_Ans" not in st.session_state:
# #     st.session_state.Gen_Ans = False
# # if "Gen_PDF" not in st.session_state:
# #     st.session_state.Gen_PDF = False
# # if "Answer" not in st.session_state:
# #     st.session_state.Answer = None

# # # Get user input
# # st.session_state.question = st.text_input("Enter Your Question:(NOTE: please enter one word since it's in training phase)", value=st.session_state.question).upper()
        
# # # Select custom font
# # font_options = [
# #     'Arial', 'Times New Roman', 'Courier New', 'Verdana',
# #     'Helvetica', 'Georgia', 'Comic Sans MS', 'Impact', 'Tahoma',
# #     'Brush Script MT', 'Lucida Handwriting', 'Papyrus', 'Segoe Script'
# #     # Add more fonts as needed
# # ]
# # st.session_state.font_family = st.selectbox("Select Font Family:", font_options, index=font_options.index(st.session_state.font_family))
        
# # col1, col2 = st.columns(2)
        
# # with col1:
# #     heading_color = st.selectbox("select Header Color:", ["#393b3d", "blue"])
# # with col2:
# #     text_color = st.selectbox("Select Font Color:", ["#307bd1", "#393b3d"])

# # # Button to generate the answer
# # gen_answer = st.button("Generate Answer")

# # # Generate answer when the button is clicked
# # if gen_answer:
# #     st.session_state.Gen_Ans = True
# #     st.session_state.Gen_PDF = False  # Reset the PDF generation state
# #     # Add a placeholder
# #     latest_iteration = st.empty()
# #     bar = st.progress(0)

# #     for i in range(100):
# #         # Update the progress bar with each iteration.
# #         latest_iteration.text(f'Loading ....')
# #         bar.progress(i + 1)
# #         time.sleep(0.1)
    
# #     st.session_state.Answer = generate_answer(st.session_state.question)
# #     latest_iteration.text(f'Loading Complete')

# # if st.session_state.Gen_Ans and st.session_state.Answer:
# #     answer = st.session_state.Answer

# #     # with col3:
# #     #     st.title(st.session_state.question)
# #     #     st.write(answer)
# #         # Display answer in HTML format
# #     st.markdown(
# #             f"<h1 style='font-family:{st.session_state.font_family};'>{st.session_state.question}</h1><p style='font-family:{st.session_state.font_family}'>{answer}</p>",
# #             unsafe_allow_html=True)
# #     st.balloons()

# #     gen_pdf = st.button("Generate PDF")

# #     if gen_pdf:
# #         st.session_state.Gen_PDF = True

# # if st.session_state.Gen_PDF:
# #     latest_iteration = st.empty()
# #     bar = st.progress(0)
# #     for i in range(100):
# #         # Update the progress bar with each iteration.
# #         latest_iteration.text(f'Generating PDF ....')
# #         bar.progress(i + 1)
# #         time.sleep(0.2)
# #     latest_iteration.text(f'Done')

# #     answer = st.session_state.Answer
# #     if answer:
# #         try:
# #             pdf_file_path = generate_pdf(st.session_state.question, answer, name, rno, sec, sub, assign_num, st.session_state.font_family)
# #             if pdf_file_path:
# #                 st.success("PDF generated successfully!")
# #                 with open(pdf_file_path, "rb") as f:
# #                     pdf_contents = f.read()
# #                     base64_pdf = base64.b64encode(pdf_contents).decode("utf-8")
# #                     # Display download link
# #                     download_link = f'<a href="data:application/pdf;base64,{base64_pdf}" download="Output.pdf">Download PDF</a>'
# #                     st.markdown(download_link, unsafe_allow_html=True)
# #                     st.balloons()
# #         except Exception as e:
# #             st.error("Error generating PDF: {}".format(e))
# #     else:
# #         st.error("Error generating PDF.")

# # st.write("To Give feedback click the below option !")
# # st.page_link("pages/4_🧾_feedback.py", label="Give Feedback", icon="🧾")
# # st.info("""Our application is still in training phase, so it may encounter occasional errors or inaccuracies.
# #     We value your feedback to help improve and refine its performance. Please take a moment to share your thoughts by navigating to the feedback section in the sidebar. Your input is greatly appreciated!""")






