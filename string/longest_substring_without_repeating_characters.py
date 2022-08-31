"""
Given a string s, find the length of the longest substring without repeating characters.

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""

test_case = "dvcd"

# O(n)
def get_longest_substring(s: str) -> int:
    max_length = 0
    if len(s) == 0:
        return 0
    if len(s) == 1:
        return 1
    sub_string = s[0]
    l = 0
    r = l + 1
    while r < len(s):
        if s[r] not in sub_string:
            sub_string += s[r]
            r += 1
        else:
            l += 1
            r = l + 1
            sub_string = s[l]

        if len(sub_string) > max_length:
            max_length = len(sub_string)

    return max_length


def test_answer():
    assert get_longest_substring(test_case) == 3


if __name__ == "__main__":
    get_longest_substring(test_case)