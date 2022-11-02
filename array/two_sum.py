"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
{7: 0}

"""

# O(n)
def get_sum(nums: list, target: int):
    nums_scores = {}
    # for i in range(len(nums)):
    #     nums_scores[target - nums[i]] = i
    #
    # for i in range(len(nums)):
    #     if nums[i] in nums_scores.keys() and nums_scores[nums[i]] != i:
    #         target = nums_scores[nums[i]]
    #         return [i, target]

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in nums_scores:
            return [i, nums_scores[complement]]
        nums_scores[nums[i]] = i


def test_two_sum():
    test_case = [2, 7, 11, 15]
    target = 9
    assert get_sum(test_case, target) == [0, 1] or get_sum(test_case, target) == [1, 0]


TEST_CASE = [2, 7, 11, 15]


# sliding windows O(n)
def get_sum2(nums: list, target: int):
    for l in range(len(nums)):
        r = l + 1
        while r <= (len(nums) - 1):
            if nums[l] + nums[r] == target:
                return [l, r]
            r += 1


def test_two_sum_sliding_windows():
    target = 9
    assert get_sum2(TEST_CASE, target) == [0, 1]


