# Profile 

profile_eng = """Enter english introduction text here"""
profile_de = """Enter german introduction text here"""

profile_dict = {
    "English": profile_eng,
    "Deutsch": profile_de,
}

# Contact details
contact_keys = ["title", "email", "phone", "address", "linkedin", "github", "publications", "details"]
contact_eng = [
    "Contact details",
    "📧 Email",
    "📱 Mobile",
    "📍 Address",
    "💼 LinkedIn",
    "🐈‍⬛🐙 GitHub",
    "📄 Publications",
    { 
    "email": "yourmail@domain.com",
    "phone": "e.g., +49 123 4567 8900",
    "address": "City, Country in english",
    "linkedin": "linkedin.com/in/yourname/",
    "github": "github.com/yourname",
    "publications": "enter here the link to your publications, if any",
    },
]
contact_de = [
    "Kontaktdaten",
    "📧 E-Mail",
    "📱 Mobil",
    "📍 Adresse",
    "💼 LinkedIn",
    "🐈‍⬛🐙 GitHub",
    "📄 Publikationen",
    {
    "email": "yourmail@domain.com",
    "phone": "e.g., +49 123 4567 8900",
    "address": "City, Country in german",
    "linkedin": "linkedin.com/in/yourname/",
    "github": "github.com/yourname",
    "publications": "enter here the link to your publications, if any",
    },
]

contact_dict = {
    "English": dict(zip(contact_keys, contact_eng)), 
    "Deutsch": dict(zip(contact_keys, contact_de)),
}

# Work experience
work_experience_keys = ["title", "company", "period", "location", "keywords", "description"]
work_experience_eng = {
    "work_experience_1": [
        "Job title in english 1", 
        "Company 1", 
        "Starting date - Finshing date, if not present", 
        "City, Country in english", 
        ":primary-background[*keyword 1 • keyword 2 • keyword 3 • keyword 4 • keyword 5 • keyword 6 • keyword 7 • keyword 8 • keyword 9 • keyword 10*]",
       """
        - enter text in english here 
        - enter text in english here
        - enter text in english here
        - enter text in english here 
        - enter text in english here
    """,
    ],
    "work_experience_2": [
        "Job title in english 2", 
        "Company 2", 
        "Starting date - Finshing date", 
        "City, Country in english", 
        ":primary-background[*keyword 1 • keyword 2 • keyword 3 • keyword 4 • keyword 5 • keyword 6 • keyword 7 • keyword 8 • keyword 9 • keyword 10*]",
       """
        - enter text in english here 
        - enter text in english here
        - enter text in english here
        - enter text in english here 
        - enter text in english here
    """,
    ],
    "work_experience_3": [
        "Job title in english 3", 
        "Company 3", 
        "Starting date - Finshing date", 
        "City, Country in english", 
        ":primary-background[*keyword 1 • keyword 2 • keyword 3 • keyword 4 • keyword 5 • keyword 6 • keyword 7 • keyword 8 • keyword 9 • keyword 10*]",
       """
        - enter text in english here 
        - enter text in english here
        - enter text in english here
        - enter text in english here 
        - enter text in english here
    """,
    ],
    "work_experience_4": [
        "Job title in english 4", 
        "Company 4", 
        "Starting date - Finshing date", 
        "City, Country in english", 
        ":primary-background[*keyword 1 • keyword 2 • keyword 3 • keyword 4 • keyword 5 • keyword 6 • keyword 7 • keyword 8 • keyword 9 • keyword 10*]",
       """
        - enter text in english here 
        - enter text in english here
        - enter text in english here
        - enter text in english here 
        - enter text in english here
    """,
    ],
}
work_experience_de = {
    "work_experience_1": [
        "Job title in german 1", 
        "Company 1", 
        "Starting date - Finshing date, if not present", 
        "City, Country in german", 
        ":primary-background[*keyword 1 • keyword 2 • keyword 3 • keyword 4 • keyword 5 • keyword 6 • keyword 7 • keyword 8 • keyword 9 • keyword 10*]",
       """

        - enter text in german here 
        - enter text in german here
        - enter text in german here
        - enter text in german here 
        - enter text in german here
    """,
    ],
    "work_experience_2": [
        "Job title in german 2", 
        "Company 2", 
        "Starting date - Finshing date", 
        "City, Country in german", 
        ":primary-background[*keyword 1 • keyword 2 • keyword 3 • keyword 4 • keyword 5 • keyword 6 • keyword 7 • keyword 8 • keyword 9 • keyword 10*]",
       """
        - enter text in german here 
        - enter text in german here
        - enter text in german here
        - enter text in german here 
        - enter text in german here
    """,
    ],
    "work_experience_3": [
        "Job title in german 3", 
        "Company 3", 
        "Starting date - Finshing date", 
        "City, Country in german", 
        ":primary-background[*keyword 1 • keyword 2 • keyword 3 • keyword 4 • keyword 5 • keyword 6 • keyword 7 • keyword 8 • keyword 9 • keyword 10*]",
       """
        - enter text in german here 
        - enter text in german here
        - enter text in german here
        - enter text in german here 
        - enter text in german here
    """,
    ],
    "work_experience_4": [
        "Job title in german 4", 
        "Company 4", 
        "Starting date - Finshing date", 
        "City, Country in german", 
        ":primary-background[*keyword 1 • keyword 2 • keyword 3 • keyword 4 • keyword 5 • keyword 6 • keyword 7 • keyword 8 • keyword 9 • keyword 10*]",
       """
        - enter text in german here 
        - enter text in german here
        - enter text in german here
        - enter text in german here 
        - enter text in german here
    """,
    ],
}

work_experience_dict = {
    "English": {k: dict(zip(work_experience_keys, v)) for k, v in work_experience_eng.items()},
    "Deutsch": {k: dict(zip(work_experience_keys, v)) for k, v in work_experience_de.items()},
}

# Achievements
achievements_eng = """
    - enter text in english here 
    - enter text in english here
    - enter text in english here
    - enter text in english here 
    - enter text in english here
    """
achievements_de = """
    - enter text in german here 
    - enter text in german here
    - enter text in german here
    - enter text in german here 
    - enter text in german here
    """

achievements_dict = {
    "English": achievements_eng,
    "Deutsch": achievements_de,
}

# Skills
skills_keys = ["category", "input"]
skills_eng = {
    "skills_1": ["Skills category 1 in english", "skill 1 in english, ..., skill x in english"],
    "skills_2": ["Skills category 2 in english", "skill 1 in english, ..., skill x in english"],
    "skills_3": ["Skills category 3 in english", "skill 1 in english, ..., skill x in english"],
    "skills_4": ["Skills category 4 in english", "skill 1 in english, ..., skill x in english"],
    "skills_5": ["Skills category 5 in english", "skill 1 in english, ..., skill x in english"],
    "skills_6": ["Skills category 6 in english", "skill 1 in english, ..., skill x in english"],
    "skills_7": ["Skills category 7 in english", "skill 1 in english, ..., skill x in english"],
}
skills_de = {
    "skills_1": ["Skills category 1 in german", "skill 1 in german, ..., skill x in german"],
    "skills_2": ["Skills category 2 in german", "skill 1 in german, ..., skill x in german"],
    "skills_3": ["Skills category 3 in german", "skill 1 in german, ..., skill x in german"],
    "skills_4": ["Skills category 4 in german", "skill 1 in german, ..., skill x in german"],
    "skills_5": ["Skills category 5 in german", "skill 1 in german, ..., skill x in german"],
    "skills_6": ["Skills category 6 in german", "skill 1 in german, ..., skill x in german"],
    "skills_7": ["Skills category 7 in german", "skill 1 in german, ..., skill x in german"],
}

skills_dict = {
    "English": {k: dict(zip(skills_keys, v)) for k, v in skills_eng.items()},
    "Deutsch": {k: dict(zip(skills_keys, v)) for k, v in skills_de.items()},
}

# Education
education_keys = ["studies", "institution", "period", "location"]
education_eng = {
    "education_1": [
        "Studies 1 in english", 
        "Institution 1", 
        "Starting date - Finshing date, if not present", 
        "City, Country in english",
    ],
    "education_2": [
        "Studies 2 in english", 
        "Institution 2", 
        "Starting date - Finshing date", 
        "City, Country in english",
    ],
    "education_3": [
        "Studies 3 in english", 
        "Institution 3", 
        "Starting date - Finshing date", 
        "City, Country in english",
    ],
    "education_4": [
        "Studies 4 in english", 
        "Institution 4",  
        "Starting date - Finshing date", 
        "City, Country in english",
    ],
}
education_de = {
    "education_1": [
        "Studies 1 in german", 
        "Institution 1",  
        "Starting date - Finshing date, if not present", 
        "City, Country in german",
    ],
    "education_2": [
        "Studies 2 in german", 
        "Institution 2", 
        "Starting date - Finshing date", 
        "City, Country in german",
    ],
    "education_3": [
        "Studies 3 in german", 
        "Institution 3",  
        "Starting date - Finshing date", 
        "City, Country in german",
    ],
    "education_4": [
        "Studies 4 in german", 
        "Institution 4", 
        "Starting date - Finshing date", 
        "City, Country in german",
    ],
}

education_dict = {
    "English": {k: dict(zip(education_keys, v)) for k, v in education_eng.items()},
    "Deutsch": {k: dict(zip(education_keys, v)) for k, v in education_de.items()},
}