import streamlit as st 
import PyPDF2  #allows Python to read PDF files.

st.title("AI & Job Analyzer")
st.write("Analyze your resume against a job description")
st.subheader("Upload Your Resume")

resume = st.file_uploader("Upload Your Resume",
                 type = ["pdf"])

if resume:
    pdf_reader = PyPDF2.PdfReader(resume)
    
    st.write("Resume uploaded successfully!")
    st.write("Number of pages:", len(pdf_reader.pages))
    
    resume_text =""
    
    for page in pdf_reader.pages:
     text = page.extract_text()
     resume_text+=text 

    st.write("Resume text:")
    st.write(resume_text) 