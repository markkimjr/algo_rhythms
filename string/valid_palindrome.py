"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
"""

TEST = "A man, a plan, a canal: Panama"


def get_solution(s: str) -> bool:
    filtered = []
    for c in s.replace(" ", ""):
        if c.isalnum():
            filtered.append(c.lower())

    filtered_reverse = filtered[::-1]

    return True if filtered == filtered_reverse else False


def test_solution():
    assert get_solution(TEST) is True


if __name__ == "__main__":
    get_solution(TEST)