"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Input: nums = [1,2,3,1]
Output: true
"""

test_case = [1, 2, 3, 1]

def check_duplicate(nums: list) -> bool:
    contains_duplicate = False
    counter = set()

    for i in range(len(nums)):
        if nums[i] in counter:
            contains_duplicate = True
            break
        counter.add(nums[i])

    return contains_duplicate


def test_check_duplicate():
    assert check_duplicate(test_case) is True

