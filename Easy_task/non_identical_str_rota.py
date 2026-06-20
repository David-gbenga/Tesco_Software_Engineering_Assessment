from typing import Optional


def is_non_identical_rotation(s1: str, s2: str) -> int:
    """
    Return 1 if s2 is a rotation of s1 but not identical to s1.
    Otherwise return 0.

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    # Lengths must match
    if len(s1) != len(s2):
        return 0

    # Must not be identical
    if s1 == s2:
        return 0

    # Rotation check
    return 1 if s2 in (s1 + s1) else 0