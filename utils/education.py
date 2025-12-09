import streamlit as st


def education(studies: str, institution: str, period: str, location: str):

    """ 
    Prints a block of text, referring to the education gathered from one course 
    of study.
    
    Parameters:
    ----------------------------------------------------------------------------
    studies: str; the course of study
    institution: str; the name of the institution the studies were accomplished 
    period: str; the time period of studying
    location: str; the location of the institution
    ----------------------------------------------------------------------------
   
    """

    st.subheader(studies)
    st.write(f"**{institution}**")
    st.caption(f"{period} {location}")