import streamlit as st
import wikipedia as wk
import pdfkit
import base64
from streamlit.errors import StreamlitAPIException
import time

st.set_page_config(
    page_title="Assignment_writer",
    page_icon="🤖",
    layout='wide'
)


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


def generate_pdf(question, answer, name, rno, sub, assign_num, font_family="Arial", ):
    try:
        # Generate HTML content for PDF with custom font
        html_content = f"<div style='padding-bottom:300px;border: 1px solid transparent'><h1 " \
                       f"style='font-size:70px;font-family:Lucida Handwriting;text-align:center" \
                       f";margin:400px 100px 0 100px;'>{sub}</h1><h2 style='margin-bottom: 300px;font-family:Lucida " \
                       f"Handwriting;text-align:center'>Assignment-{assign_num}</h2>" \
                       f"<div style='width:100%;height:250px;margin-bottom:10px;border:1px solid " \
                       f"transparent;padding-top:100px'><p " \
                       f"style='text-align: right;text-decoration: " \
                       f"underline;font-size:25px;font-family:{font_family};color:{heading_color};'>{name}</p><p " \
                       f"style='text-align: right;text-decoration: " \
                       f"underline;font-size:25px;font-family:{font_family};color:{heading_color};'>{rno}</p></div>" \
                       f"<div style='border: 1px solid transparent;padding-top:50px'><h1 style='font-family:{font_family};color:{heading_color};text-decoration:underline;" \
                       f"padding:30px'>{question}</h1><p style='font-family:{font_family};color" \
                       f":{text_color};font-size:25px;line-height: 2.0'>{answer}</p></div></div>"

        # Specify PDF options
        pdf_options = {
            'quiet': '',
            'page-size': 'A4',
            'margin-top': '0.75in',
            'margin-right': '0.75in',
            'margin-bottom': '0.75in',
            'margin-left': '0.75in',
            'encoding': "UTF-8",
        }

        # Convert HTML to PDF
        config = pdfkit.configuration(wkhtmltopdf=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe')
        pdf_file_path = "output.pdf"
        pdfkit.from_string(html_content, pdf_file_path, options=pdf_options, configuration=config)
        return pdf_file_path
    except Exception as e:
        st.error("Error generating PDF: {}".format(e))
    except StreamlitAPIException as e:
        # Handle the exception gracefully
        st.error("An error occurred while rendering the content. Please try again later.")


# sidebar
st.sidebar.info('Fill this form for Your front page details', icon="ℹ️")
with st.sidebar.form("form1", clear_on_submit=True, border=True):
    name = st.text_input("Enter Your Name: ")
    rno = st.text_input("Emter Your Roll No: ")
    sub = st.text_input("Enter Your subject title: ")
    assign_num = st.selectbox("Select Assignment number: ", [1, 2])
    btn = st.form_submit_button("Submit")

# Streamlit UI
st.title("Assignment Writer App")
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
        pdf_file_path = generate_pdf(question, answer, name, rno, sub, assign_num, font_family)
        if pdf_file_path:
            st.success("PDF generated successfully!")
            with open(pdf_file_path, "rb") as f:
                base64_pdf = base64.b64encode(f.read()).decode('utf-8')
                pdf_display = f'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="700" ' \
                              f'type="application/pdf" filename="Output.pdf">'
                st.markdown(pdf_display, unsafe_allow_html=True)
        st.balloons()

    else:
        st.error("Error generating PDF.")


