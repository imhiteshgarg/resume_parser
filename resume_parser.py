from extractors import extract_email, extract_name, extract_phone_number, extract_skills
from utilities import extract_text_from_docx, extract_text_from_pdf

def parse_resume(file_path):
    # Extract text based on file type
    if file_path.endswith('.pdf'):
        text = extract_text_from_pdf(file_path)
    elif file_path.endswith('.docx'):
        text = extract_text_from_docx(file_path)
    else:
        return None
    
    print('text',text)
    # Extract details
    name = extract_name(text)
    email = extract_email(text)
    phone = extract_phone_number(text)
    skills = extract_skills(text)

    # Return parsed information
    return {
        "Name": name,
        "Email": email,
        "Phone": phone,
        "Skills": skills
    }

# Example Usage
parsed_data = parse_resume("resume.pdf")
print(parsed_data)
