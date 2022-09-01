"""
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.
"""

TEST_INPUT = "ABABBA"
K = 2


# O(n)
def get_solution(s: str, k: int) -> int:
    max_length = 0
    counter = {}
    l = 0
    for r in range(len(s)):
        counter[s[r]] = counter.get(s[r], 0) + 1

        if (r - l + 1) - max(counter.values()) > k:
            counter[s[l]] -= 1
            l += 1

        max_length = max(max_length, r - l + 1)

    return max_length


def test_solution():
    assert get_solution(TEST_INPUT, K) == 5