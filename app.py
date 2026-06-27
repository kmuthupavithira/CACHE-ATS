import streamlit as st
import recruiter
import applicant

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="CACHE",
    page_icon="🎯",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==========================================================
# CUSTOM CSS
# ==========================================================

st.markdown("""
<style>

/* Hide Streamlit Menu */
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

/* Background */

.stApp{
    background:#F5F7FA;
}

/* Title */

.title{
    text-align:center;
    font-size:60px;
    font-weight:700;
    color:#111827;
    margin-bottom:5px;
}

/* Subtitle */

.subtitle{
    text-align:center;
    font-size:23px;
    color:#6B7280;
    margin-bottom:30px;
}

/* Banner */

.banner{

    background:linear-gradient(90deg,#111827,#374151);

    padding:35px;

    border-radius:20px;

    color:white;

    text-align:center;

    margin-bottom:30px;

}

.banner h1{

    font-size:55px;

    margin-bottom:5px;

}

.banner p{

    font-size:20px;

}

/* Portal Card */

.portal{

    background:white;

    border-radius:18px;

    padding:20px;

    text-align:center;

    box-shadow:0px 5px 12px rgba(0,0,0,.10);

}

/* Feature Card */

.feature{

    background:white;

    border-radius:18px;

    padding:18px;

    height:155px;

    box-shadow:0px 4px 10px rgba(0,0,0,.08);

    transition:.3s;

    margin-bottom:25px;

}

.feature:hover{

    transform:translateY(-5px);

    box-shadow:0px 8px 18px rgba(0,0,0,.15);

}

.feature h3{

    color:#111827;

}

.feature p{

    color:#4B5563;

}

/* Buttons */

.stButton > button{

    width:100%;

    height:55px;

    background:#111827;

    color:white;

    border:none;

    border-radius:12px;

    font-size:18px;

    font-weight:bold;

}

.stButton > button:hover{

    background:black;

    color:white;

}

/* Footer */

.footer{

    text-align:center;

    color:gray;

    font-size:15px;

    margin-top:30px;

}

</style>
""", unsafe_allow_html=True)
# ==========================================================
# HEADER
# ==========================================================

st.markdown("""
<div class="banner">

<h1>🎯 CACHE</h1>

<p>Candidate Analysis & Competency Hiring Engine</p>

</div>
""", unsafe_allow_html=True)

# ==========================================================
# DASHBOARD
# ==========================================================

st.subheader("🚀 Dashboard")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("📄 Resume Screening")

with col2:
    st.success("📊 ATS Score")

with col3:
    st.warning("🏆 Resume Ranking")

with col4:
    st.error("🧠 Skill Analysis")

st.write("")

# ==========================================================
# PORTAL
# ==========================================================

st.subheader("Choose Your Portal")

# Session State

if "portal" not in st.session_state:
    st.session_state.portal = "Recruiter"

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
<div class="portal">
<h2>👨‍💼 Recruiter</h2>
<br>

</div>
""", unsafe_allow_html=True)

    if st.button("Open Recruiter", use_container_width=True):
        st.session_state.portal = "Recruiter"

with col2:

    st.markdown("""
<div class="portal">
<h2>👩‍🎓 Applicant</h2>
<br>

</div>
""", unsafe_allow_html=True)

    if st.button("Open Applicant", use_container_width=True):
        st.session_state.portal = "Applicant"

portal = st.session_state.portal

st.divider()
# ==========================================================
# WHY CHOOSE CACHE
# ==========================================================

st.markdown("## ⭐ Why to Choose CACHE?")

# ---------------- FIRST ROW ----------------

col1, col2, col3 = st.columns(3, gap="large")

with col1:

    st.markdown("""
    <div class="feature">

    <h3>📄 Resume Screening</h3>

    <p>
    Upload multiple resumes and compare them with the Job Description using AI-powered analysis.
    </p>

    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="feature">

    <h3>📊 ATS Score</h3>

    <p>
    Automatically calculate ATS compatibility scores for every uploaded resume.
    </p>

    </div>
    """, unsafe_allow_html=True)

with col3:

    st.markdown("""
    <div class="feature">

    <h3>🏆 Resume Ranking</h3>

    <p>
    Rank candidates automatically from the highest ATS score to the lowest.
    </p>

    </div>
    """, unsafe_allow_html=True)

# ---------------- SPACE ----------------

st.markdown("<div style='height:25px;'></div>", unsafe_allow_html=True)

# ---------------- SECOND ROW ----------------

col4, col5, col6 = st.columns(3, gap="large")

with col4:

    st.markdown("""
    <div class="feature">

    <h3>🧠 Skill Analysis</h3>

    <p>
    Detect matched skills and identify missing keywords from the job description.
    </p>

    </div>
    """, unsafe_allow_html=True)

with col5:

    st.markdown("""
    <div class="feature">

    <h3>📈 Analytics</h3>

    <p>
    Generate recruiter summaries and compare candidate performance instantly.
    </p>

    </div>
    """, unsafe_allow_html=True)

with col6:

    st.markdown("""
    <div class="feature">

    <h3>📥 CSV Reports</h3>

    <p>
    Export ATS rankings and screening reports with a single click.
    </p>

    </div>
    """, unsafe_allow_html=True)

st.divider()
# ==========================================================
# LOAD SELECTED PORTAL
# ==========================================================

st.markdown("## 🚀 Workspace")

if portal == "Recruiter":

    st.success("👨‍💼 Recruiter Portal")

    recruiter.recruiter_portal()

else:

    st.success("👩‍🎓 Applicant Portal")

    applicant.applicant_portal()


# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.markdown("""

<div class="footer">

<h2 style="color:#111827;margin-bottom:5px;">
🎯 CACHE
</h2>

<p style="font-size:18px;">
Candidate Analysis & Competency Hiring Engine
</p>
<p>

🐍 Python &nbsp; | &nbsp;
🌐 Streamlit &nbsp; | &nbsp;
🤖 Scikit-Learn &nbsp; | &nbsp;
📄 OCR
</p>

<p>

</p>

<p>
© 2026 CACHE
</p>

</div>

""", unsafe_allow_html=True)