"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
"""

TEST = ["eat","tea","tan","ate","nat","bat"]

# brute force TODO find correct solution
def group_anagrams(strs: list) -> list:
    solution = []
    tracker = {}

    for word in strs:
        if tracker.get(len(word)):
            tracker[len(word)].append(word)
        else:
            tracker[len(word)] = [word]

    total_tracker = {}
    for length, words in tracker.items():
        for word in words:
            c_counter = {word: {}}
            for c in word:
                c_counter[word][c] = c_counter[word][c].get(c, 0) + 1

            if total_tracker.get(length):
                total_tracker[length].append(c_counter)
            else:
                total_tracker[length] = [c_counter]

    for length, counted_words in total_tracker.items():
        pass


if __name__ == "__main__":
    group_anagrams(TEST)