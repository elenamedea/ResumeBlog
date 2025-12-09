import streamlit as st
from utils import print_markdown as md

def work_experience(title: str, company: str, period: str, location: str, keywords: str, description: str):

    """ 
    Prints a block of text, referring to the work experience gathered from one 
    position.
    
    Parameters:
    ----------------------------------------------------------------------------
    title: str; the title of the position
    company: str; the name of the company the work experience acquired 
    period: str; the time period working under this position
    keywords: str; main skills performed
    location: str; the location of the company and working environment
    description: str; the main points describing your work routine, structured 
    bullet points
    ----------------------------------------------------------------------------
   
    """
    st.subheader(title)
    st.write(f"**{company}**")
    st.caption(f"{period} {location}")
    st.caption(f"{keywords}")
    md(description)