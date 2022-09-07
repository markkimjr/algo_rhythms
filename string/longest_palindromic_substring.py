"""
Given a string s, return the longest palindromic substring in s.

Input: s = "bbbbdbbbb"
Output: "bab"
Explanation: "aba" is also a valid answer.
"""

TEST = "bbbbdbbbb"
import requests

# O(n^3)
def get_solution(s: str) -> str:
    if len(s) == 1:
        return s
    record_string = ""

    for l in range(len(s)):
        for r in range(1, len(s)):
            sub_string = s[l: r+1]
            if sub_string == sub_string[::-1]:
                if len(sub_string) > len(record_string):
                    record_string = sub_string

    return record_string

# O(n^2) TODO REVIEW!
def get_solution2(s: str) -> str:
    res = ""
    res_len = 0

    for i in range(len(s)):
        l, r = i, i
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > res_len:
                res = s[l:r+1]
                res_len = r - l + 1
            l -= 1
            r += 1

        l, r = i, i + 1
        while l >= 0 and r < len(s) and s[l] == s[r]:
            if (r - l + 1) > res_len:
                res = s[l:r+1]
                res_len = r - l + 1
            l -= 1
            r += 1

    return res
