"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

A substring is a contiguous sequence of characters within the string.

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
"""

TEST_S = "abc"
TEST_T = "bc"


# TODO find correct solution
def get_solution(s: str, t: str) -> str:
    if s == "":
        return ""
    if len(t) == 1:
        if t in s:
            return t
        else:
            return ""
    l = 0
    s_counter = {}
    t_counter = {}
    possible_answers = {}

    t_length = 0
    for letter in t:
        t_length += 1
        t_counter[letter] = t_counter.get(letter, 0) + 1

    s_length = 0
    indexes = []

    for r in range(len(s)):
        if s[r] in t:
            s_counter[s[r]] = s_counter.get(s[r], 0) + 1
            s_length += 1
            indexes.append(r)

        if s_length == t_length:
            contains_all = True
            for letter in t:
                if s_counter[letter] < t_counter[letter]:
                    contains_all = False
                    break

            if contains_all:
                substring = s[l:r + 1]
                possible_answers[len(substring)] = (l, r+1)
                s_counter[s[indexes[0]]] -= 1
                l = indexes[1]
                indexes.pop(0)
                s_length -= 1

    if len(possible_answers.keys()) == 0:
        return ""

    min_length = min(possible_answers.keys())
    return s[possible_answers[min_length][0]:possible_answers[min_length][1]]


def test_solution():
    assert get_solution(TEST_S, TEST_T) == "BANC"

if __name__ == "__main__":
    get_solution(TEST_S, TEST_T)