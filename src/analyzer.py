"""
src/analyzer.py
Core analysis logic — placeholder until LLM integration is added.
"""


def analyze(resume: dict, job: dict) -> dict:
    """
    Compare a parsed resume against a parsed job description.
    Returns placeholder results for now; will be replaced with LLM calls.
    """
    return {
        "match_score": 72,
        "missing_skills": [
            "Docker",
            "Kubernetes",
            "AWS / GCP / Azure",
            "Microservices architecture",
        ],
        "weak_bullets": [
            "Helped fix bugs in the API",
            "Attended team meetings and wrote documentation",
        ],
        "improved_bullets": [
            "Resolved 15+ API bugs, reducing error rate by 20% across core endpoints",
            "Authored internal documentation adopted by 3 engineering teams",
        ],
        "tailored_summary": (
            "Backend-focused software engineer with Python and API experience, "
            "seeking to bring strong fundamentals and a collaborative work style "
            "to TechCorp's platform team."
        ),
    }
