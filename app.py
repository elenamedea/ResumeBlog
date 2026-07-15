from pathlib import Path

import logfire
import streamlit as st

from utils import app_title, app_icon

# Page config — must be the first Streamlit command (streamlit >= 1.45)
st.set_page_config(
    layout = "wide",
    initial_sidebar_state = "expanded",
    page_title = app_title,
    page_icon = app_icon,
)

# Observability (optional): traces are sent only when LOGFIRE_TOKEN is set
# in the environment; without the token this is a silent no-op, so forks
# work without a Logfire account.
@st.cache_resource
def configure_logfire():
    logfire.configure(send_to_logfire = "if-token-present", service_name = "resumeblog")

configure_logfire()

# CSS styling, shared by every page; path is robust to the working directory
css = (Path(__file__).parent / "style.css").read_text()
st.markdown(f"<style>{css}</style>", unsafe_allow_html = True)

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

with logfire.span("page view: {page_title}", page_title = pg.title):
    pg.run()
