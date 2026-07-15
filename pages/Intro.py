import streamlit as st

from utils import print_markdown as md

from utils import badge_name, latest_project_link

# Title
st.title("🪴 Welcome to my resume website 🪴")
# Name badge
st.badge(badge_name, color = "primary")

# App summary
md("""
Hello, and thank you for visiting!  
This website presents my professional journey, in an interactive way.  

You can explore my **Curriculum Vitae** and **Contact details** in your preferred language:

- 🌐 [**English**](CV_eng) section
- 🌐 [**German**](CV_de) section

Simply select your preferred language above or use the navigation menu on the left to switch 
between sections.
""")
st.divider()

col_extra1, col_extra2 = st.columns([0.5, 0.5], gap = "medium")

# First column of extras
with col_extra1:
    # Latest project section
    st.subheader("🚀 Latest project")
    md("""I am always excited developing new coding projects.  
                    Check out my **latest one** here:""")
    st.link_button("👉 View project", latest_project_link, type = "primary")
# Second column of extras
with col_extra2:
    # Fun fallback
    st.subheader("♟️ Play a game of chess ♟️")
    md("In case the site is under maintenance, why not enjoy a quick game of chess?")

    st.link_button("⏱️ Start Game", "https://www.chess.com/play", type = "primary")
