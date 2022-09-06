"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.

Input: s = "()"
Output: true
"""
from collections import deque

TEST = "()[]{}"
TEST_2 = "{[()]}"


def get_solution(s: str) -> bool:
    if len(s) % 2 != 0:
        return False

    stack = []

    check = {
        ")": "(",
        "]": "[",
        "}": "{"
    }

    for c in s:
        if c in check:
            if stack and check[c] == stack[-1]:
                stack.pop()
            else:
                return False
        else:
            stack.append(c)

    return True if not stack else False

def check_solution():
    assert get_solution(TEST) is True


if __name__ == "__main__":
    get_solution(TEST)
