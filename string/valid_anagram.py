"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: s = "anagram", t = "nagaram"
Output: true
"""

TEST_S = "anagram"
TEST_T = "nagaram"


# O(n)
def check_valid_anagram(s: str, t: str) -> bool:
    tracker_s = {}
    tracker_t = {}
    for c in s:
        tracker_s[c] = tracker_s.get(c, 0) + 1
    for c in t:
        tracker_t[c] = tracker_t.get(c, 0) + 1
    if tracker_s == tracker_t:
        return True
    return False


def test_solution():
    assert check_valid_anagram(TEST_S, TEST_T) is True

