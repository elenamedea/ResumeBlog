import streamlit as st

from utils import print_header as header
from utils import print_markdown as md
from utils import title_caption_links as app_intro
from utils import work_experience as we
from utils import skills as sk
from utils import education as edu

from utils import name
from utils import profile_dict, contact_dict, work_experience_dict, achievements_dict, skills_dict, education_dict

# Language selection
lang = "Deutsch"

# Title, caption, and tabs with useful links
contact = contact_dict[lang]

app_intro(name, 
          contact["details"]["address"], 
          contact["details"]["phone"], 
          contact["details"]["email"],
          f"""https://www.{contact["details"]["linkedin"]}""", "💼", 
          f"""https://{contact["details"]["github"]}""", "💻", 
          f"""https://www.{contact["details"]["publications"]}""", "📄",
          tab3 = "Publikationen")

# App summary
profile = profile_dict[lang]

header("Profil")
md(profile)

# Work experience section
experience = work_experience_dict[lang]

header("Berufserfahrung")

col_we1, col_we2 = st.columns([0.5, 0.5], gap = "medium")
## First column of the work experience
with col_we1: 
    ### 1. eolos GmbH
    we(
        experience["work_experience_1"]["title"],
        experience["work_experience_1"]["company"],
        experience["work_experience_1"]["period"],
        experience["work_experience_1"]["location"],
        experience["work_experience_1"]["keywords"],
        experience["work_experience_1"]["description"],
    )
    st.divider()
    ### 2. Unreal estate GmbH
    we(
        experience["work_experience_2"]["title"],
        experience["work_experience_2"]["company"],
        experience["work_experience_2"]["period"],
        experience["work_experience_2"]["location"],
        experience["work_experience_2"]["keywords"],
        experience["work_experience_2"]["description"],
    )
## Second column of the work experience
with col_we2: 
    ### 3. Spoty labs
    we(
        experience["work_experience_3"]["title"],
        experience["work_experience_3"]["company"],
        experience["work_experience_3"]["period"],
        experience["work_experience_3"]["location"],
        experience["work_experience_3"]["keywords"],
        experience["work_experience_3"]["description"],
    )
    st.divider()
    ### 4. Georg-August-Universität Göttingen
    we(
        experience["work_experience_4"]["title"],
        experience["work_experience_4"]["company"],
        experience["work_experience_4"]["period"],
        experience["work_experience_4"]["location"],
        experience["work_experience_4"]["keywords"],
        experience["work_experience_4"]["description"],
    )

# Achievements section
achievements = achievements_dict[lang]

header("Erfolge")
md(achievements)

# Skills section
skills = skills_dict[lang]

header("Fähigkeiten")

col_sk1, col_sk2 = st.columns([0.5, 0.5], gap = "medium")
## First column of skills
with col_sk1:
    ### Programming languages
    sk(skills["skills_1"]["category"], skills["skills_1"]["input"])
    ### Frameworks and libraries
    sk(skills["skills_2"]["category"], skills["skills_2"]["input"])
    ### Databases, tools, etc
    sk(skills["skills_3"]["category"], skills["skills_3"]["input"])
    ### Version control, CI/CD, cloud and hosting
    sk(skills["skills_4"]["category"], skills["skills_4"]["input"])
## Second column of skills
with col_sk2:
    ### ML concepts
    sk(skills["skills_5"]["category"], skills["skills_5"]["input"])
    ### Lab skills
    sk(skills["skills_6"]["category"], skills["skills_6"]["input"])
    ### Languages
    sk(skills["skills_7"]["category"], skills["skills_7"]["input"])

# Education section
education = education_dict[lang]

header("Bildung")

col_e1, col_e2 = st.columns([0.5, 0.5], gap = "medium")
## First column of education
with col_e1: 
    ### 1. Spiced academy
    edu(
        education["education_1"]["studies"],
        education["education_1"]["institution"],
        education["education_1"]["period"],
        education["education_1"]["location"],
        )
    st.divider()
    ### 2. IU Akademie
    edu(
        education["education_2"]["studies"],
        education["education_2"]["institution"],
        education["education_2"]["period"],
        education["education_2"]["location"],
        )
## Second column of education
with col_e2: 
    ### 3. PhD
    edu(
        education["education_3"]["studies"],
        education["education_3"]["institution"],
        education["education_3"]["period"],
        education["education_3"]["location"],
        )
    st.divider()
    ### 4. Diploma
    edu(
        education["education_4"]["studies"],
        education["education_4"]["institution"],
        education["education_4"]["period"],
        education["education_4"]["location"],
        )