import cohere

co = cohere.Client("TAZ6h9NXXZeGWoycT3tMSwAttVDmQ6TQ8lTWPNqS")  # Replace with your API key

def get_resume_feedback(resume_text, job_description):
    prompt = f"""
You are a professional resume reviewer.

Job Description:
{job_description}

Resume:
{resume_text}

Please provide a detailed, constructive review of this resume based on the job description. Mention areas of improvement and whether the resume is a good fit for the role.
"""

    response = co.chat(
        model="command-r-plus",  # Most powerful model
        message=prompt,
        temperature=0.7
    )

    return response.text
