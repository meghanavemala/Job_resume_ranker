# 📝 Job Resume Ranker & Feedback System

An intelligent NLP-powered web app that ranks resumes based on how well they match a given job description — and gives constructive feedback on the best one. Built with **Streamlit**, **sentence-transformers**, and **Cohere's LLM**.

---

## 🚀 Features

- 📥 Upload a **job description** (`.txt`)  and multiple **resumes** (`.pdf` or `.txt`)
- 📊 Ranks resumes by **semantic similarity**
- 🤖 Generates **personalized feedback** for the top resume using **Cohere's LLM**
- ⚡ Built with **modern NLP**: sentence embeddings + cosine similarity
- 🌐 Simple, interactive web interface with **Streamlit**

---

## 🧠 How It Works

### 1. Data Upload & Preprocessing
- Users upload a **job description** and **resumes**
- Text is extracted and cleaned (via regex + PyPDF2)

### 2. Semantic Ranking
- Uses `all-MiniLM-L6-v2` from `sentence-transformers` to embed text
- Computes **cosine similarity** between each resume and the job description
- Resumes are sorted based on similarity score

### 3. Feedback Generation
- The top-matching resume is sent to **Cohere's `command-r-plus` API**
- It returns a **constructive, job-specific review** with suggestions

---

## 🛠 Tech Stack

| Component         | Tool/Library                         |
|------------------|--------------------------------------|
| NLP Embedding    | `sentence-transformers`              |
| Semantic Scoring | `scikit-learn` (cosine similarity)   |
| PDF Parsing      | `PyPDF2`                             |
| LLM Feedback     | `Cohere API`                         |
| Frontend UI      | `Streamlit`                          |
| Text Cleaning    | `re` (regular expressions)           |

---

## 🧪 How to Run Locally

1. **Clone the repository:**

```bash
git clone https://github.com/yourusername/resume-ranker.git
cd resume-ranker
````

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Add your Cohere API key** in `cohere_feedback.py`:

```python
co = cohere.Client("YOUR_API_KEY")
```

4. **Run the app:**

```bash
streamlit run app.py
```

---

## 📦 File Structure

```
resume-ranker/
├── app.py                 # Main Streamlit app
├── utils.py               # File reading, cleaning, ranking functions
├── cohere_feedback.py     # LLM feedback generation
├── requirements.txt
└── README.md
```

---

## 🔮 Future Improvements

* Generate feedback for **all** resumes, not just the top one
* Visualize **skill/keyword overlaps**
* Export **PDF reports**
* Support **.docx** files
* Add **user accounts** and session history

---

## 🎓 Learning Outcomes

This project demonstrates how **NLP + AI** can:

* Automate manual HR processes
* Provide fair and semantic resume screening
* Help candidates improve applications with contextual feedback

---

## 📌 Live Demo

👉 Try it here: [Job_Resume_Ranker_App 🌐](https://jobresumeranker-lfq6bnfxuuh9gns2xarwmw.streamlit.app/)

---

