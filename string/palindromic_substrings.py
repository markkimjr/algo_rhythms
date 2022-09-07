"""
Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""

TEST = "abcabc"
TEST2 = "abba"

# O(n^2) TODO REVIEW!
def get_solution(s: str) -> int:
    res = 0
    for i in range(len(s)):
        l, r = i, i
        l, r, res = slide_windows(l, r, s, res)

        l = i
        r = i + 1
        l, r, res = slide_windows(l, r, s, res)

    return res


def slide_windows(l: int, r: int, s: str, res: int):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        res += 1
        l -= 1
        r += 1
    return l, r, res


if __name__ == "__main__":
    get_solution(TEST2)
