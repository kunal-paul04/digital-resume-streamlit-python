from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Kunal's Resume.pdf"
profile_pic = current_dir / "assets" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Kunal Kanti Paul"
PAGE_ICON = ":wave:"
NAME = "Kunal Kanti Paul"
DESCRIPTION = """
Assistant Manager (Software Development) at Digital India Corporation.
"""
EMAIL = "kunalkantipaul@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/kunal-kanti-paul-26b92a98/",
    "GitHub": "https://github.com/kunal-paul04",
}
PROJECTS = {
    "🏆 MY Bharat - Working on web services for MY Bharat (Mera Yuva Bharat) under Ministry of Youth Affairs. Developing and managing user account service (includes user registration and login) by using Python, PHP.": "https://mybharat.gov.in/",
    "🏆 Parinaam Manjusha - Parinam Majusha is a digital academic repository launched by CBSE in 2016 which allows students to get their mark sheets, pass and migration certificates in digital form and facilitates their online verification by employers and educational institutions. It is developed using PHP, MySQL in Codeigniter 3 framework.": "https://cbse.digitallocker.gov.in/",
    "🏆 National Academic Depository (NAD) - National Academic Depository (NAD) is an online depository to Academic institutions to store and publish their academic awards. It is developed using PHP, MySQL, Python in Codeigniter 3 framework.": "https://nad.digilocker.gov.in/",
}


st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qulifications")
st.write(
    """
- ✔️ 4+ Years of expereince in software development
- ✔️ Completed Master of Computer Application from Assam Science and Technology University, Guwahati
- ✔️ Strong hands on experience and knowledge in Python and PHP
- ✔️ Good understanding of statistical principles and their respective applications
- ✔️ Excellent team-player and displaying strong sense of initiative on tasks
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- 🖥️ Front End & Back End Development: Python, JavaScript, HTML, CSS, Ajax, PHP
- 📊 Programming Framework: Codeigniter, Laravel, Flask API, FastAPI
- 🗄️ Database and Query Languages: MySQL, MongoDB
- 📚 Miscellaneous: API Development, GIT, Redis, Elastic Stack (ELK), RabbitMQ, Amazon AWS S3
"""
)


# --- WORK EXPERIENCE ---
st.write('\n')
st.subheader("Work Experience")
st.write("---")

# --- JOB 1
st.write("🏢", "**Deputy Manager (Software Development) | Digital India Corporation**")
st.write("Mar 2022 - Present")
st.write(
    """
Working as a Software Developer at Digital India Corporation under Ministry of Electronics and Information Technology.
- ► Working on DigiLocker, National Academic Depository (NAD), MY Bharat under National E-Governance Division.
- ► Developed and implemented a highly efficient and scalable software solution,reducing manual data entry time by 50% and improving overall productivity.
- ► Collaborated with a cross-functional team to design and execute a complex client-server application, resulting in a seamless user experience and increased customer satisfaction. Identified and resolved critical software bugs, ensuring optimal performance and reliability of the application, and minimizing downtime for end users.
- ► Led the integration of a third-party API into the existing software infrastructure, enabling seamless data exchange and expanding functionality, resulting in a 20% increase in user engagement.
"""
)

# --- JOB 2
st.write('\n')
st.write("🏢", "**Digital Marketing Executive | D.R Brijmohan & Sons Pvt. Ltd**")
st.write("Dec 2020 - Feb 2022")
st.write(
    """
Responsible for increasing sale of the company through digital media. Promoting company products through digital platforms: Facebook, Instagram, Indiamart, Amazon, etc. Also responsible for maintaining sale analysis reporting and company internal workflow systems (FMS - Flow chart monitoring system of each work process).
\nKey Responsibilities:
- ► Boosting sale advertisement and generating customer leads from digital platforms.
- ► Managing the internal workflow systems of the company.
"""
)

# --- JOB 3
st.write('\n')
st.write("🏢", "**Software Developer | Technowell Services PVT. LTD.**")
st.write("Dec 2018 - Nov 2020")
st.write(
    """
Worked with project management staff to capture requirements for the functional elements of website projects. Also responsible for liaising with clients and ensuring that all work carried out complies with standards and guidelines.
\nKey Responsibilities:
- ► Building PHP websites using Object Oriented Programming.
- ► Testing and validating work produced as part of the development process.
- ► Developing web sites using MySQL, PHP, AJAX & other programming tools.
"""
)


# --- Projects ---
st.write('\n')
st.subheader("Projects")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


# --- CERTIFICATIONS ---
st.write('\n')
st.subheader("Certifications")
st.write("---")
st.write("👨‍🎓", "**APIs with Postman for Absolute Beginners | Udemy**")
st.write("👨‍🎓", "**JavaScript 2019: JavaScript ES6 Certification Course | Udemy**")
