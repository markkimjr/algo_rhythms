"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
"""

test_case = [-2, 1, -3, 4, -1, 2, 1, -5, 4]


# brute force (pre answer lookup)
def get_maximum_subarray(nums: list) -> int:
    max_score = 0
    local_score = 0
    left_pointer = 0
    right_pointer = 1
    end_index = len(nums) - 1
    restart_needed = False
    while left_pointer <= end_index:
        if restart_needed:
            local_score = 0
        restart_needed = False
        # starting score is always first left pointer (might only be one item in array)
        if left_pointer == 0:
            max_score = nums[left_pointer]
        if local_score == 0:
            local_score = nums[left_pointer]

        # if index is outside of list index, break
        if right_pointer > end_index:
            if local_score > max_score:
                max_score = local_score
            break
        if nums[right_pointer] < 0:
            if left_pointer == 0:
                if abs(nums[right_pointer]) >= abs(nums[left_pointer]):
                    left_pointer = right_pointer + 1
                    right_pointer += 2
                    restart_needed = True
            else:
                if abs(nums[left_pointer]) < abs(nums[right_pointer]):
                    left_pointer = right_pointer + 1
                    right_pointer += 2
                    restart_needed = True
                else:
                    local_score += nums[right_pointer]
                    right_pointer += 1
        else:
            if left_pointer == 0:
                if nums[left_pointer] < 0 and nums[right_pointer] > 0:
                    if abs(nums[left_pointer]) >= abs(nums[right_pointer]):
                        left_pointer = right_pointer
                        right_pointer += 1
                        restart_needed = True
            else:
                local_score += nums[right_pointer]
                right_pointer += 1

        if local_score > max_score:
            max_score = local_score

    return max_score


def test_max_subarray():
    assert get_maximum_subarray(test_case) == 6

# TODO search answer and refactor

