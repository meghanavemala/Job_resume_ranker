import streamlit as st
from utils import read_file, rank_resumes, clean_text
from cohere_feedback import get_resume_feedback

st.title("📝 Job Resume Ranker & Feedback System")

job_file = st.file_uploader("Upload Job Description (.txt)", type=['txt'])
resume_files = st.file_uploader("Upload Resumes (PDF or TXT)", type=['pdf', 'txt'], accept_multiple_files=True)

if job_file and resume_files:
    job_text = clean_text(read_file(job_file))
    resumes = {file.name: clean_text(read_file(file)) for file in resume_files}

    if st.button("Rank Resumes"):
        st.subheader("📊 Resume Ranking:")
        ranking = rank_resumes(job_text, resumes)
        for rank, (name, score) in enumerate(ranking, 1):
            st.write(f"**{rank}. {name}** — Similarity Score: `{score:.2f}`")

        st.subheader("📢 Feedback:")
        top_resume_name, _ = ranking[0]
        feedback = get_resume_feedback(resumes[top_resume_name], job_text)
        st.markdown(f"**Top Resume: {top_resume_name}**")
        st.markdown(feedback)
else:
    st.info("Please upload both a job description and at least one resume.")
