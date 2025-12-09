import streamlit as st

from utils import app_title, app_icon

# Intro section 
intro_page = st.Page("./pages/Intro.py", title = "Welcome!", icon = "🪴")

# English section
english_pages = [
    st.Page("./pages/CV_eng.py", title = "Curriculum Vitae", icon = "📑"),
    st.Page("./pages/contact_eng.py", title = "Contact", icon = "📨")
]

# German section
german_pages = [
    st.Page("./pages/CV_de.py", title = "Curriculum Vitae", icon = "📑"),
    st.Page("./pages/contact_de.py", title = "Kontakt", icon = "📨")
] 

# Page structure
pg = st.navigation(
    {
        "Home": [intro_page], 
        "English": english_pages,
        "Deutsch": german_pages,
    }
)
# Page config
st.set_page_config(
    layout = "wide", 
    initial_sidebar_state = "expanded", 
    page_title = app_title, 
    page_icon = app_icon,
)

pg.run()