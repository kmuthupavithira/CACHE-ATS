import streamlit as st
import pandas as pd

from utils import extract_text
from recruiter import calculate_score

# -----------------------------
# Same Skills Database
# -----------------------------

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

# -----------------------------
# Applicant Portal
# -----------------------------

def applicant_portal():

    st.header("👩‍🎓 Applicant Portal")

    st.write("Upload your resume and compare it with a Job Description.")

    job_desc = st.text_area(
        "Paste Job Description",
        height=220,
        placeholder="Paste Job Description Here..."
    )

    uploaded_file = st.file_uploader(
        "Upload Resume",
        type=["pdf", "docx"]
    )

    if st.button("Analyze My Resume"):

        if uploaded_file is None:
            st.warning("Please upload your resume.")
            return

        if job_desc.strip() == "":
            st.warning("Please paste the Job Description.")
            return

        # -----------------------------
        # Extract Resume
        # -----------------------------

        resume_text = extract_text(uploaded_file)

        if resume_text.strip() == "":
            st.error("Unable to extract text from the resume.")
            return

        # -----------------------------
        # ATS Score
        # -----------------------------

        score, matched_skills = calculate_score(
            job_desc,
            resume_text
        )

        # -----------------------------
        # Missing Skills
        # -----------------------------

        missing_skills = []

        resume_lower = resume_text.lower()
        job_lower = job_desc.lower()

        for skill in SKILLS:

            if skill in job_lower and skill not in resume_lower:
                missing_skills.append(skill)

        # -----------------------------
        # Status
        # -----------------------------

        if score >= 80:
            status = "🟢 Excellent Match"

        elif score >= 60:
            status = "🟡 Good Match"

        else:
            status = "🔴 Needs Improvement"

        # -----------------------------
        # Results
        # -----------------------------

        st.subheader("📊 ATS Result")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("ATS Score", f"{score}%")

        with col2:
            st.metric("Status", status)

        st.progress(score / 100)

        # -----------------------------
        # Matched Skills
        # -----------------------------

        st.subheader("✅ Matched Skills")

        if matched_skills:

            for skill in matched_skills:
                st.success(skill.title())

        else:
            st.warning("No matching skills found.")

        # -----------------------------
        # Missing Skills
        # -----------------------------

        st.subheader("❌ Missing Skills")

        if missing_skills:

            for skill in missing_skills:
                st.error(skill.title())

        else:
            st.success("No important skills are missing.")

        # -----------------------------
        # Suggestions
        # -----------------------------

        st.subheader("💡 Resume Suggestions")

        suggestions = []

        if len(missing_skills) > 0:

            suggestions.append(
                "Add the missing technical skills if you have experience with them."
            )

        if "project" not in resume_lower:
            suggestions.append(
                "Include at least 2 academic or personal projects."
            )

        if "internship" not in resume_lower:
            suggestions.append(
                "Add internship experience if available."
            )

        if "github" not in resume_lower:
            suggestions.append(
                "Include your GitHub profile."
            )

        if "certification" not in resume_lower:
            suggestions.append(
                "Mention relevant certifications."
            )

        if "achievement" not in resume_lower:
            suggestions.append(
                "Include technical achievements or coding profiles."
            )

        if len(suggestions) == 0:

            st.success(
                "Excellent Resume! It is well aligned with the Job Description."
            )

        else:

            for suggestion in suggestions:
                st.info(suggestion)

        # -----------------------------
        # Resume Preview
        # -----------------------------

        with st.expander("📄 View Extracted Resume Text"):

            st.text(resume_text[:5000])

        # -----------------------------
        # Download Report
        # -----------------------------

        report = pd.DataFrame([{

            "Resume": uploaded_file.name,

            "ATS Score": score,

            "Status": status,

            "Matched Skills": ", ".join(matched_skills),

            "Missing Skills": ", ".join(missing_skills)

        }])

        st.download_button(

            "📥 Download ATS Report",

            report.to_csv(index=False),

            file_name="Applicant_ATS_Report.csv",

            mime="text/csv"

        )