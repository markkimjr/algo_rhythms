"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
"""

test_case = [1, 2, 3, 4]

# brute force O(n^2)
def get_product_of_array_except_self(nums: list) -> list:
    answer = []
    for i in range(len(nums)):
        total_product = 1
        for s in range(len(nums)):
            if i == s:
                continue
            total_product *= nums[s]
        answer.append(total_product)
    return answer

# brute force test
def test_brute_force_answer():
    assert get_product_of_array_except_self(test_case) == [24, 12, 8, 6]


# TODO O(n)
