"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

from collections import defaultdict

TEST = ["eat","tea","tan","ate","nat","bat"]


# O(m * n)
def group_anagrams(strs: list) -> list:
    solution = defaultdict(list)
    for w in strs:
        count = [0] * 26

        for c in w:
            count[ord(c) - ord("a")] += 1

        solution[tuple(count)].append(w)

    return list(solution.values())


if __name__ == "__main__":
    group_anagrams(TEST)