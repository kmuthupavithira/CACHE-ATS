import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from utils import extract_text
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# ----------------------------------------------------
# Skills Database
# ----------------------------------------------------

SKILLS = [
    "python",
    "java",
    "c",
    "sql",
    "mysql",
    "html",
    "css",
    "javascript",
    "git",
    "github",
    "flask",
    "django",
    "streamlit",
    "machine learning",
    "data structures",
    "algorithms",
    "oop",
    "numpy",
    "pandas",
    "scikit-learn",
    "communication",
    "problem solving",
    "rest api"
]

# ----------------------------------------------------
# ATS Score Calculation
# ----------------------------------------------------

def calculate_score(job_desc, resume_text):

    tfidf = TfidfVectorizer(stop_words="english")

    matrix = tfidf.fit_transform([job_desc.lower(), resume_text.lower()])

    similarity = cosine_similarity(
        matrix[0:1],
        matrix[1:2]
    )[0][0]

    similarity_score = similarity * 70

    matched_skills = []

    for skill in SKILLS:
        if skill in job_desc.lower() and skill in resume_text.lower():
            matched_skills.append(skill)

    jd_skill_count = sum(1 for skill in SKILLS if skill in job_desc.lower())

    if jd_skill_count > 0:
        skill_score = (len(matched_skills) / jd_skill_count) * 30
    else:
        skill_score = 0

    final_score = round(similarity_score + skill_score, 2)

    if final_score > 100:
        final_score = 100

    return final_score, matched_skills


# ----------------------------------------------------
# Recruiter Portal
# ----------------------------------------------------

def recruiter_portal():

    st.header("👨‍💼 Recruiter Portal")

    st.subheader("📝 Enter Job Description")

    job_desc = st.text_area(
        "Job Description",
        height=220,
        placeholder="Paste the Job Description here..."
    )

    uploaded_files = st.file_uploader(
        "Upload Multiple Resumes (PDF/DOCX)",
        type=["pdf", "docx"],
        accept_multiple_files=True
    )

    if st.button("Analyze Resumes"):

        if job_desc.strip() == "":
            st.warning("Please enter the Job Description.")
            return

        if not uploaded_files:
            st.warning("Please upload resumes.")
            return

        results = []

        selected = 0
        shortlisted = 0
        rejected = 0

        progress = st.progress(0)

        for i, file in enumerate(uploaded_files):

            resume_text = extract_text(file)

            if resume_text.strip() == "":
                continue

            score, matched_skills = calculate_score(
                job_desc,
                resume_text
            )

            if score >= 80:
                status = "Selected"
                selected += 1

            elif score >= 60:
                status = "Shortlisted"
                shortlisted += 1

            else:
                status = "Rejected"
                rejected += 1

            results.append({

                "Resume": file.name,

                "ATS Score": score,

                "Status": status,

                "Matched Skills": ", ".join(matched_skills)

            })

            progress.progress((i + 1) / len(uploaded_files))

        if len(results) == 0:
            st.error("No readable resumes found.")
            return

        df = pd.DataFrame(results)

        df = df.sort_values(
            by="ATS Score",
            ascending=False
        )

        # --------------------------
        # Ranking Table
        # --------------------------

        st.subheader("🏆 Resume Ranking")

        st.dataframe(
            df,
            use_container_width=True
        )

        # --------------------------
        # Summary Cards
        # --------------------------

        st.subheader("📊 Recruitment Summary")

        c1, c2, c3 = st.columns(3)

        c1.metric("🟢 Selected", selected)
        c2.metric("🟡 Shortlisted", shortlisted)
        c3.metric("🔴 Rejected", rejected)

        # --------------------------
        # ATS Score Graph
        # --------------------------

        st.subheader("📈 ATS Score Comparison")

        fig, ax = plt.subplots(figsize=(10,5))

        ax.bar(
            df["Resume"],
            df["ATS Score"]
        )

        ax.set_xlabel("Candidates")
        ax.set_ylabel("ATS Score")
        ax.set_ylim(0,100)

        plt.xticks(rotation=45)

        st.pyplot(fig)

        # --------------------------
        # Summary Table
        # --------------------------

        summary = pd.DataFrame({

            "Status":[
                "🟢 Selected",
                "🟡 Shortlisted",
                "🔴 Rejected"
            ],

            "Number of Candidates":[
                selected,
                shortlisted,
                rejected
            ]

        })

        st.subheader("📋 Overall Recruitment Summary")

        st.table(summary)

        # --------------------------
        # Download CSV
        # --------------------------

        st.download_button(

            "📥 Download ATS Report",

            df.to_csv(index=False),

            file_name="ATS_Report.csv",

            mime="text/csv"

        )