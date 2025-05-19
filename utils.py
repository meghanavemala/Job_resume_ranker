import re
from sentence_transformers import SentenceTransformer, util
from PyPDF2 import PdfReader

# Load the sentence transformer model once
model = SentenceTransformer('all-MiniLM-L6-v2')

def read_file(file):
    """
    Reads uploaded PDF or TXT file-like object from Streamlit.
    """
    if file.name.endswith('.pdf'):
        reader = PdfReader(file)
        text = ''
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
        return text
    else:  # .txt file
        return file.read().decode('utf-8')

def clean_text(text):
    """
    Cleans text by stripping whitespace and reducing extra spaces.
    """
    return re.sub(r'\s+', ' ', text).strip().lower()

def rank_resumes(job_description, resumes):
    """
    Ranks resumes based on cosine similarity with job description.
    """
    jd_embedding = model.encode(job_description, convert_to_tensor=True)
    ranked = []

    for filename, text in resumes.items():
        resume_embedding = model.encode(text, convert_to_tensor=True)
        score = util.cos_sim(jd_embedding, resume_embedding).item()
        ranked.append((filename, score))

    return sorted(ranked, key=lambda x: x[1], reverse=True)