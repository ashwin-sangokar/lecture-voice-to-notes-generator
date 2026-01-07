import re

def extract_key_points(text: str, max_points: int = 5):
    """
    Extracts key points from text using rule-based approach
    Returns a list of bullet points
    """

    if not text or len(text.strip()) == 0:
        return []

    # Split text into sentences
    sentences = re.split(r'(?<=[.!?]) +', text)

    # Basic filtering rules
    cleaned = [
        s.strip()
        for s in sentences
        if len(s.split()) > 6
    ]

    # Pick top N sentences as key points
    key_points = cleaned[:max_points]

    return key_points
