"""
app.py
AI Resume Analyzer — Streamlit frontend.
"""

import streamlit as st
from src.resume_parser import parse_resume
from src.job_parser import parse_job_description
from src.analyzer import analyze
from src.utils import is_empty

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(page_title="AI Resume Analyzer", page_icon="📄", layout="wide")

# ── Header ───────────────────────────────────────────────────────────────────
st.title("📄 AI Resume Analyzer")
st.markdown(
    "Paste your resume and a job description below. "
    "The analyzer will score your match, surface missing skills, "
    "and suggest stronger bullet points."
)
st.divider()

# ── Input columns ────────────────────────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    st.subheader("Your Resume")
    resume_text = st.text_area(
        label="resume_input",
        placeholder="Paste your resume here...",
        height=350,
        label_visibility="collapsed",
    )

with col2:
    st.subheader("Job Description")
    job_text = st.text_area(
        label="job_input",
        placeholder="Paste the job description here...",
        height=350,
        label_visibility="collapsed",
    )

st.divider()

# ── Analyze button ────────────────────────────────────────────────────────────
if st.button("Analyze Resume", type="primary", use_container_width=True):

    # Validate inputs
    if is_empty(resume_text) and is_empty(job_text):
        st.warning("Please paste both a resume and a job description.")
    elif is_empty(resume_text):
        st.warning("Please paste your resume.")
    elif is_empty(job_text):
        st.warning("Please paste a job description.")
    else:
        # Parse and analyze
        resume = parse_resume(resume_text)
        job = parse_job_description(job_text)
        results = analyze(resume, job)

        st.divider()
        st.subheader("Analysis Results")

        # ── Match Score ───────────────────────────────────────────────────────
        score = results["match_score"]
        color = "green" if score >= 75 else "orange" if score >= 50 else "red"
        st.metric(label="Match Score", value=f"{score}%")
        st.progress(score / 100)

        st.divider()

        # ── Two-column results layout ─────────────────────────────────────────
        left, right = st.columns(2)

        with left:
            # Missing skills
            st.markdown("#### Missing Skills")
            for skill in results["missing_skills"]:
                st.markdown(f"- {skill}")

            st.markdown("")

            # Weak bullets
            st.markdown("#### Weak Resume Bullets")
            for bullet in results["weak_bullets"]:
                st.markdown(f"- _{bullet}_")

        with right:
            # Improved bullets
            st.markdown("#### Improved Bullets")
            for bullet in results["improved_bullets"]:
                st.markdown(f"- {bullet}")

            st.markdown("")

            # Tailored summary
            st.markdown("#### Tailored Summary")
            st.info(results["tailored_summary"])
