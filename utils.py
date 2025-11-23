import re

def extract_likes(aria_label_text):
    """
    Extrahiert die Anzahl der Likes aus einem aria-label Text.

    Args:
    aria_label_text (str): Der aria-label Text, z.B. "Ich mag das Video (wie 6.812 andere auch)"

    Returns:
    str: Die extrahierte Anzahl der Likes, z.B. "6812"
    """
    match = re.search(r'wie ([\d,.]+) andere', aria_label_text)
    if match:
        likes = match.group(1).replace('.', '')
        return likes
    return None


def extract_date(date):
    """
    Extrahiert das Datum aus dem Text.

    Args:
    date (str): z.B. "Am 30.06.2013 beigetreten"

    Returns:
    str: Das Datum
    """
    match = re.search(r'Am (\d{2}\.\d{2}\.\d{4}) beigetreten', date)
    if match:
        extracted_date = match.group(1)
        return extracted_date
    return None
