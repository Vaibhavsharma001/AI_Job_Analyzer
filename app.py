import streamlit as st 
import PyPDF2  #allows Python to read PDF files.

skills = [
    "python",
    "java",
    "javascript",
    "react",
    "html",
    "css",
    "sql",
    "mongodb",
    "git",
    "github",
    "streamlit",
    "django",
    "flask",
    "fastapi",
    "machine learning",
    "data science",
    "aws",
    "docker",
    "kubernetes",
    "jenkins",
    "redis",
    "postgresql",
    "linux",
    "azure"
]

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
    
  
st.subheader("Job description")
job_description = st.text_area(
    "Paste job description here"
    ,height = 250)

if st.button("Analyze Resume"): 
    
    if not resume:
        st.warning("Upload your resume")
        
    elif not job_description:
        st.warning("Please enter a job description.")
        
    else:
        resume_lower = resume_text.lower()
        job_lower = job_description.lower()

        st.write("Resume text length:", len(resume_lower))
        st.write("Job description length:", len(job_lower))

        matching_skills = []

        for skill in skills:
            if skill in resume_lower and skill in job_lower:
                matching_skills.append(skill)

        missing_skills = []

        for skill in skills:
            if skill in job_lower and skill not in resume_lower:
                missing_skills.append(skill)

        st.subheader("Matching Skills")

        if matching_skills:
            st.write(matching_skills)
        else:
            st.write("No matching skills found.")

        st.subheader("Missing Skills")

        if missing_skills:
            st.write(missing_skills)
        else:
            st.write("No missing skills found")

        total_required_skills = len(matching_skills) + len(missing_skills)

        if total_required_skills > 0:
            ats_score = (len(matching_skills) / total_required_skills) * 100
        else:
            ats_score = 0

        st.subheader("ATS SCORE")
        st.write(f"{ats_score:.0f}%")