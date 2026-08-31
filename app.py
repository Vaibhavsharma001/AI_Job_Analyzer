import streamlit as st 

st.title("AI & Job Analyzer")
st.write("Analyze your resume against a job description")
st.subheader("Upload Your Resume")

resume = st.file_uploader("Upload Your Resume",
                 type = ["pdf"])

