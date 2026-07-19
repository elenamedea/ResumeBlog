import streamlit as st


def title_caption_links(title: str, location: str, phone: str, mail: str,
                        button1_link: str, button1_icon, button2_link: str, button2_icon,
                        button3_link: str, button3_icon, button1: str = "LinkedIn",
                        button2: str = "GitHub", button3: str = "Publications",
                        button_type: str = "primary"):

    """
    Prints a block of text, referring to the title of the Streamlit page, its
    caption and a row of three useful link buttons, displayed side by side.

    Parameters:
    ------------------------------------------------------------------------------
    title: str; the title of Streamlit page, in this resume app is recommended to
    use the name of the person to whom the CV is referring to
    location: str; address details
    phone: str; phone number with the country code (recommended)
    mail: str; e-mail address

    button1: str, default value is "LinkedIn"; label of the first button
    button1_link: str; link to be associated with the first button
    button1_icon: str; icon to be associated with the first button

    button2: str, default value is "GitHub"; label of the second button
    button2_link: str; link to be associated with the second button
    button2_icon: str; icon to be associated with the second button

    button3: str, default value is "Publications"; label of the third button
    button3_link: str; link to be associated with the third button
    button3_icon: str; icon to be associated with the third button

    button_type: str, default value is "primary"; type of the link button
    ----------------------------------------------------------------------------

    """
    # Title and caption
    st.title(title)
    st.caption(f"{location} | {phone} | {mail}")

    # Row of useful links, buttons side by side
    with st.container(horizontal = True, gap = "small"):
        st.link_button(f"**{button1}**", button1_link, icon = button1_icon, type = button_type)
        st.link_button(f"**{button2}**", button2_link, icon = button2_icon, type = button_type)
        st.link_button(f"**{button3}**", button3_link, icon = button3_icon, type = button_type)
