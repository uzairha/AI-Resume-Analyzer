"""
src/job_parser.py
Extracts structured fields from a raw job description.
"""


def parse_job_description(text: str) -> dict:
    """
    Parse raw job description text into structured fields.
    Returns a dict with keys: raw, word_count, char_count.
    """
    return {
        "raw": text.strip(),
        "word_count": len(text.split()),
        "char_count": len(text),
    }
