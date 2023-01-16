from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV.pdf"
profile_pic = current_dir / "assets" / "ala_ceo.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Gustav B"
PAGE_ICON = ":wave:"
NAME = "Gustav Bagus Samanta"
DESCRIPTION = """
I am passionate about learning new things to improve myself. Seeking to leverage development and collaboration as a data analyst or data scientist.
"""
EMAIL = "gustavsmnt@gmail.com"
SOCIAL_MEDIA = {
    "👔LinkedIn": "https://www.linkedin.com/in/gustavsmnt/",
    "🤖GitHub": "https://github.com/gustavsmnt"
}
PROJECTS = {
    "🏆 Classification Analysis using CNN and LSTM on Wheezing Sounds - International Journal on Information and Communication Technology (IJoICT)": "https://socj.telkomuniversity.ac.id/ojs/index.php/ijoict/article/view/621",
    "🏆 AIRBNB Singapore Listing Analysis Project - Final Project of DQLAB Data Analyst Bootcamp": "https://gustavsmnt-airbnb-project-project-airbnb-uszn1j.streamlit.app/",
    
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
    st.image(profile_pic, width=250)

with col2:
    st.markdown("""
    <h5 style='text-align: left; ;font-size: 30px;'>Gustav Bagus Samanta</h5>"""
    , unsafe_allow_html=True)
    st.markdown("""
    <h5 style='text-align: left; ;font-size: 18px;'>Bachelor of Computer Science</h5>"""
    , unsafe_allow_html=True)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    #st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(3)
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
     cols[index].write(f"[{platform}]({link})")
cols[2].write("📩gustavsmnt@gmail.com")


# # --- EXPERIENCE & QUALIFICATIONS ---
# st.write('\n')
# st.subheader("Qualification")
# st.write(
#     """
# - ✔️ 10 Years experience scrolling through Twitter
# - ✔️ Strong hands on experience and knowledge in shopping online using Tokopedia
# - ✔️ Good understanding and communication
# - ✔️ Excellent team-player and displaying strong sense of initiative on tasks
# """
# )


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write("---")
st.write(
    """
- 👩‍💻 Programming: Python, SQL, Pascal, C++, LaTeX
- 📊 Data Visulization: Plotly, Streamlit, MS Excel, PowerBI
- 🗄️ Databases: Oracle, MySQL, Postgre
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Experience")
st.write("---")

# --- JOB 1
st.write("🚧", "**PRODUCTION SYSTEM INTERNSHIP | PT. Suzuki Indomobil Motor Indonesia**")
st.write("06/2019 - 07/2019")
st.write(
    """
- ► Managed two-wheel vehicle production and assembling database
- ► Organized the production database 
- ► Evaluated and ensured production results are achieved in terms of quantity and quality
- ► Created the internship reports for presentation on campus
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**DATA ANNOTATOR FREELANCE | Warung Pintar**")
st.write("07/2020 - 08/2020")
st.write(
    """
- ► Completed a total of 500 image annotations with 50 image annotations per day for 10 days (working days)
- ► Ensured the image objects are properly labeled/annotated
- ► Email the completed image annotations, or directly via flash or hard drive
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**RUNNER EVENT 2ND ICC-OSH | PT. Wahana Kendali Mutu**")
st.write("06/2022")
st.write(
    """
- ► Created an event rundown
- ► Handled events to ensure the participants who attend can take part in all existing event activities
- ► Helped the participants, judges, and speakers sending the files needed during the event
- ► Managed the event before the event started until the event is over
"""
)
# --- JOB 4
st.write('\n')
st.write("🚧", "**ADMIN OFFICER | Auto Mitsuda**")
st.write("02/2022 - 07/2022")
st.write(
    """
- ► Managed schedule for students and mentors
- ► Created daily courses reports
- ► Handled visitors, guests, and customers as well as direct and answer questions by telephone to handle customer complaints politely and professionally
- ► Managed daily finances both incoming and outgoing for operations
"""
)
# --- JOB 5
st.write('\n')
st.write("🚧", "**INTERNAL SEMINAR SPEAKER | Telkom University Faculty of Informatics**")
st.write("09/2022")
st.write(
    """
- ► Presented the journal publications Classification Analysis using CNN and LSTM on Wheezing Sounds

"""
)

# --- EDUCATION ---
st.write('\n')
st.subheader("Education")
st.write("---")
st.write('\n')
st.write("🎓", "**COMPUTER SCIENCE BACHELOR DEGREE, Telkom University**")
st.write("2015 - 2022")
st.write(
    """
- ► Conducted an Undergraduate Thesis the Classification Analysis using CNN and LSTM on Wheezing Sounds
- ► 517 points of English Proficiency Test on Telkom University (B1 CEFR)
"""
)

# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Projects & Publication")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
