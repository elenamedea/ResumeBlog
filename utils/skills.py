import streamlit as st
from utils import print_markdown as md

def skills(category: str, input: str):

    """ 
    Prints a block of text, referring to the context of a skill category.
    
    Parameters:
    ----------------------------------------------------------------------------
    category: str; the title of the skills' category
    input: str; a list of skills referring to the respective category
    ----------------------------------------------------------------------------
   
    """

    st.write(f"**{category}**")
    md(input)