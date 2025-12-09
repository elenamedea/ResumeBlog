import streamlit as st

from utils import print_header as header
from utils import print_markdown as md

from utils import contact_dict, profile_dict
from utils import contact_title, calendly_link

# Language selection
lang = "English"

# Title and App summary
st.title(contact_title)
profile = profile_dict[lang]

header("Profile")
md(profile)

# Contact details and useful links
contact = contact_dict[lang]

header(f"""{contact["title"]}""")

col_c1, col_c2 = st.columns([0.5, 0.5], gap="medium")

# First column of contact details
with col_c1:
    contact_1 = f"""
        **{contact["email"]}**  
        {contact["details"]["email"]}  

        **{contact["phone"]}**  
        {contact["details"]["phone"]}  

        **{contact["address"]}**  
        {contact["details"]["address"]}  
    """
    md(contact_1)


# Second column of contact details
with col_c2:
    contact_2 = f"""
        **{contact["linkedin"]}**  
        [{contact["details"]["linkedin"]}](https://{contact["details"]["linkedin"]})  

        **{contact["github"]}**  
        [{contact["details"]["github"]}](https://{contact["details"]["github"]})  

        **{contact["publications"]}**  
        [{contact["details"]["publications"]}](https://{contact["details"]["publications"]})
    """
    md(contact_2)

# Introductory meeting
header("Schedule a meeting :telephone_receiver: :postbox:")

st.link_button("Calendly", calendly_link, type = "primary")