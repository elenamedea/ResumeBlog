import streamlit as st


def print_markdown(summary_context: str, html_render: bool = True) -> str:

    """ 
    Takes a text and returns it as a Streamlit markdown.
    
    Parameters:
    ----------------------------------------------------------------------------
    summary_context: str; the text to be printed as a markdown
    html_render: bool, default value is True; whether to render HTML within body
    ----------------------------------------------------------------------------
   
    """
    
    summary = st.markdown(summary_context, unsafe_allow_html = html_render)

    return summary