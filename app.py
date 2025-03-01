'''import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from resume_generator import generate_resume

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_AI_KEY"))

# Function to generate AI-enhanced summary
def generate_summary(text):
    if not text.strip():
        return "Please enter some text to summarize."

    model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Gemini 1.5 Pro
    response = model.generate_content(text)
    
    return response.text

# Streamlit UI
st.title("AI-Powered Smart Resume Generator")

# User Inputs
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
address = st.text_input("Address")

summary_input = st.text_area("Enter a brief summary about yourself")
summary = ""

if st.button("Generate Summary with AI"):
    summary = generate_summary(summary_input)
    st.text_area("AI-Generated Summary", summary, height=150)

skills = st.text_area("Enter your skills (comma-separated)").split(",")

# Experience Input
experience = []
num_experiences = st.number_input("Number of Experiences", min_value=0, max_value=5, step=1)
for i in range(num_experiences):
    st.subheader(f"Experience {i+1}")
    company = st.text_input(f"Company {i+1}")
    position = st.text_input(f"Position {i+1}")
    dates = st.text_input(f"Duration {i+1} (e.g., Jan 2022 - Dec 2022)")
    location = st.text_input(f"Location {i+1}")
    details = st.text_area(f"Details {i+1} (Separate points by new lines)").split("\n")
    experience.append({"company": company, "position": position, "dates": dates, "location": location, "details": details})

# Education Input
education = []
num_education = st.number_input("Number of Education Entries", min_value=0, max_value=3, step=1)
for i in range(num_education):
    st.subheader(f"Education {i+1}")
    institution = st.text_input(f"Institution {i+1}")
    degree = st.text_input(f"Degree {i+1}")
    year = st.text_input(f"Year {i+1}")
    education.append({"institution": institution, "degree": degree, "year": year})

# Generate Resume PDF
if st.button("Generate Resume PDF"):
    resume_data = {
        "name": name,
        "email": email,
        "phone": phone,
        "address": address,
        "summary": summary,
        "skills": skills,
        "experience": experience,
        "education": education,
    }
    generate_resume(resume_data)
    st.success("Resume generated successfully! Download below:")
    with open("generated_resume.pdf", "rb") as file:
        st.download_button("Download Resume", file, file_name="Resume.pdf", mime="application/pdf")'''
import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
from resume_generator import generate_resume, summarize_text

# Load environment variables
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_AI_KEY"))

# Streamlit UI
st.title("AI-Powered Smart Resume Generator")

# User Inputs
name = st.text_input("Full Name")
email = st.text_input("Email")
phone = st.text_input("Phone Number")
address = st.text_input("Address")

github = st.text_input("GitHub Link")
linkedin = st.text_input("LinkedIn Profile")

summary_input = st.text_area("Enter a brief summary about yourself")
summary = st.text_area("AI-Generated Summary", "", height=150)  # Initialize as an editable field

if st.button("Generate Summary with AI"):
    generated_summary = summarize_text(summary_input)
    st.session_state["summary"] = generated_summary  # Store in session state
    st.rerun()  # Refresh UI

if "summary" in st.session_state:
    summary = st.session_state["summary"]
    st.text_area("AI-Generated Summary", summary, height=150)  

skills = st.text_area("Enter your skills (comma-separated)").split(",")

# Experience Input
experience = []
num_experiences = st.number_input("Number of Experiences", min_value=0, max_value=5, step=1)
for i in range(num_experiences):
    st.subheader(f"Experience {i+1}")
    company = st.text_input(f"Company {i+1}")
    position = st.text_input(f"Position {i+1}")
    dates = st.text_input(f"Duration {i+1} (e.g., Jan 2022 - Dec 2022)")
    location = st.text_input(f"Location {i+1}")
    details = st.text_area(f"Details {i+1} (Separate points by new lines)").split("\n")
    experience.append({"company": company, "position": position, "dates": dates, "location": location, "details": details})

# Education Input
education = []
num_education = st.number_input("Number of Education Entries", min_value=0, max_value=3, step=1)
for i in range(num_education):
    st.subheader(f"Education {i+1}")
    institution = st.text_input(f"Institution {i+1}")
    degree = st.text_input(f"Degree {i+1}")
    year = st.text_input(f"Year {i+1}")
    education.append({"institution": institution, "degree": degree, "year": year})

# Generate Resume Preview & Download
if st.button("Generate Resume PDF"):
    resume_data = {
        "name": name,
        "email": email,
        "phone": phone,
        "address": address,
        "summary": summary,
        "skills": skills,
        "experience": experience,
        "education": education,
        "github": github,
        "linkedin": linkedin,
    }

    pdf_path = generate_resume(resume_data)
    st.success("Resume generated successfully! Download below:")
    with open(pdf_path, "rb") as file:
        st.download_button("Download Resume", file, file_name="Resume.pdf", mime="application/pdf")
