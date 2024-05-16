import streamlit as st
import wikipedia as wk
from xhtml2pdf import pisa
import base64
from streamlit.errors import StreamlitAPIException
import time

st.set_page_config(
    page_title="frz_Assignment_writer App",
    page_icon="📝",
    layout='wide',
    initial_sidebar_state="expanded",
)


hds= """<style>
    #MainMenu {}
    footer {visibility : hidden;}
    .main {
     background-image: linear-gradient(to right, #0c1835,#052958);
     opacity: 0.8;}
    
    /* Custom sidebar text color */
    div[data-testid="stSidebarContent"] {
        background-color: #052958; /* Text color */
    }
    
    /* Custom input fields color */
    input[type="text"], input[type="number"], input[type="email"], input[type="password"], textarea, select {
        background-color: rgba(12, 24, 53, 0.8);
        color: #ffffff; /* Text color */
    }

    </style>
"""
st.markdown(hds, unsafe_allow_html=True)


def generate_answer(question):
    try:
        # Get answer from Wikipedia
        answer = wk.summary(question)
        return answer
    except wk.exceptions.DisambiguationError as e:
        return st.error("Error generating PDF: {}".format(e))
    except wk.exceptions.PageError as e:
        return st.error("Error generating PDF: {}".format(e))
    except wk.exceptions.WikipediaException:
        st.warning(
            "Error generating PDF: Wikipedia search parameter is not set. No match for an empty query.")
    except Exception as e:
        return st.error("Error generating PDF: {}".format(e))

def generate_pdf(question, answer, name, rno, sec, sub, assign_num, font_family="Arial", heading_color="#393b3d", text_color="#307bd1"):
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
                <p style="padding-top: 80px;text-align:center;font-size:28px;"><strong>{question}</strong></p>
                <p>{answer}</p>
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


st.title("Assignment Writer App")
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
        st.error("Please fill out all required fields!")
    else:
        with open("form_values.txt", "w") as file:
            st.success("Form submitted successfully!")
st.warning("Please fill the front details if not filled. Navigate to sidebar and Fill the form.")

st.write("NOTE: please enter one word since it's in training phase")
# Get user input
question = st.text_input("Enter Your Question:")
question = question.upper()
        
# Select custom font
font_options = [
    'Arial', 'Times New Roman', 'Courier New', 'Verdana',
    'Helvetica', 'Georgia', 'Comic Sans MS', 'Impact', 'Tahoma',
    'Brush Script MT', 'Lucida Handwriting', 'Papyrus', 'Segoe Script'
     # Add more fonts as needed
]
font_family = st.selectbox("Select Font Family:", font_options)
        
col1, col2 = st.columns(2)
        
with col1:
    heading_color = st.selectbox("select Header Color:", ["#393b3d", "blue"])
with col2:
    text_color = st.selectbox("Select Font Color:", ["#307bd1", "#393b3d"])
        
# Generate answer when button is clicked
if st.button("Generate Answer"):
    # Add a placeholder
    latest_iteration = st.empty()
    bar = st.progress(0)
        
    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Loading ....')
        bar.progress(i + 1)
        time.sleep(0.1)
    answer = generate_answer(question)
    latest_iteration.text(f'Loading Complete')
        
    col3, col4 = st.columns(2)
        
    with col3:
        st.title(question)
        st.write(answer)
    with col4:
        # Display answer in HTML format
        st.markdown(
            f"<h1 style='font-family:{font_family};'>{question}</h1><p style='font-family:{font_family}'>{answer}</p>",
            unsafe_allow_html=True)
        st.balloons()
        
# Generate PDF when button is clicked
if st.button("Generate PDF"):
    latest_iteration = st.empty()
    bar = st.progress(0)
    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Generating PDF ....')
        bar.progress(i + 1)
        time.sleep(0.2)
    latest_iteration.text(f'Done')
        
    answer = generate_answer(question)
    if answer:
        try:
            pdf_file_path = generate_pdf(question, answer, name, rno,sec, sub, assign_num, font_family)
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
        
st.write("To Give feedback click the below option !")
st.page_link("pages/4_🧾_feedback.py",label="Give Feedback",icon="🧾")
st.info("""Our application is still in training Phase,so it may encounter occasional errors or inaccuracies.
    We value your feedback to help improve and refine its performance. Please take a moment to share your thoughts by navigating to the feedback section in the sidebar. Your input is greatly appreciated!""")
