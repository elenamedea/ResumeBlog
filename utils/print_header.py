import streamlit as st


def print_header(context: str, div: bool | str = True) -> str:

    """ 
    Takes a text and returns it as a Streamlit markdown.
    
    Parameters:
    -------------------------------------------------------------------------------------
    context: str; the text to be printed as a header
    div: bool or str, default value is True; shows a colored divider below the header
    -------------------------------------------------------------------------------------
    """

    header = st.header(context, divider = div)
    
    return header