"""
All helper functions for AOC.
"""

def parse_int(num: str) -> int:
    """Helper for parsing integers safely - returns 0 if ValueError"""
    try:
        return int(num, 10)
    except ValueError:
        return 0
