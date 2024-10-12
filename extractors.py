import re
import spacy

nlp = spacy.load('en_core_web_sm')

# Extract email
def extract_email(text):
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    email = re.findall(email_pattern, text)
    return email[0] if email else None

# Extract phone number
def extract_phone_number(text):
    phone_pattern = re.compile(r'\b\d{10}\b|\b(?:\+?\d{1,3}[-.\s]?)?(?:\(\d{1,4}\)|\d{1,4})[-.\s]?\d{1,4}[-.\s]?\d{1,4}\b')
    phone = re.findall(phone_pattern, text)
    return phone[0] if phone else None


# Extract name using spaCy's NER
def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

skills = ["Python", "Java", "Django", "Flask", "AWS", "Docker", "Kubernetes", "SQL", "JavaScript","JIRA"]

def extract_skills(text):
    skill_set = []
    for skill in skills:
        if skill.lower() in text.lower():
            skill_set.append(skill)
    return skill_set

