# https://codechalleng.es/bites/262/
from collections import Counter


def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    c = Counter(sequence.lower())
    # total = sum(c.values())
    sum_gc = c.get("g", 0) + c.get("c", 0)
    total = sum_gc + c.get("a", 0) + c.get("t", 0)
    return round(sum_gc / total * 100, 2)
