"""
src/resume_parser.py
Extracts structured fields from raw resume text.
"""


def parse_resume(text: str) -> dict:
    """
    Parse raw resume text into structured sections.
    Returns a dict with keys: raw, word_count, char_count.
    """
    return {
        "raw": text.strip(),
        "word_count": len(text.split()),
        "char_count": len(text),
    }
