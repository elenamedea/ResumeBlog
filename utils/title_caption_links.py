import streamlit as st


def title_caption_links(title: str, location: str, phone: str, mail: str, 
                        tab1_link: str, tab1_icon, tab2_link: str, tab2_icon, 
                        tab3_link: str, tab3_icon, tab1: str = "LinkedIn", 
                        tab2: str = "GitHub", tab3: str = "Publications", 
                        tab_type: str = "primary"):

    """ 
    Prints a block of text, referring to the title of the Streamlit page, its 
    caption and a triplet of useful links.
    
    Parameters:
    ------------------------------------------------------------------------------
    title: str; the title of Streamlit page, in this resume app is recommended to 
    use the name of the person to whom the CV is referring to
    location: str; address details
    phone: str; phone number with the country code (recommended)
    mail: str; e-mail address

    tab1: str, default value is "LinkedIn"; title of the first tab
    tab1_link: str; link to be associated with the first button
    tab1_icon: str; icon to be associated with the first button

    tab2: str, default value is "GitHub"; title of the second tab
    tab2_link: str; link to be associated with the second button
    tab2_icon: str; icon to be associated with the second button

    tab3: str, default value is "Publications"; title of the third tab
    tab3_link: str; link to be associated with the third button
    tab3_icon: str; icon to be associated with the third button

    tab_type: str, default value is "primary"; type of the link button
    ----------------------------------------------------------------------------
   
    """
    # Title and caption
    st.title(title)
    st.caption(f"{location} | {phone} | {mail}")

    # Tab with useful links
    tab_1, tab_2, tab_3 = st.tabs([f"**{tab1}**", f"**{tab2}**", f"**{tab3}**"])
    with tab_1:
        st.link_button(f"**{tab1}**", tab1_link, icon = tab1_icon, type = tab_type)

    with tab_2:
        st.link_button(f"**{tab2}**", tab2_link, icon = tab2_icon, type = tab_type)

    with tab_3:
        st.link_button(f"**{tab3}**", tab3_link, icon = tab3_icon, type = tab_type)
