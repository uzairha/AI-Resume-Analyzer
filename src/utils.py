"""
src/utils.py
Shared helper utilities.
"""


def is_empty(text: str) -> bool:
    """Return True if text is None or only whitespace."""
    return not text or not text.strip()
