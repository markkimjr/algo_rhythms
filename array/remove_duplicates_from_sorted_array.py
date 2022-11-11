"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

Example
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

[0, 1, 2, 2, 2, 3, 4]
"""
from typing import List

TEST = [0, 1, 2, 2, 2, 3, 4]
TEST2 = [1, 1, 2]


class Solution:
    # neetcode solution O(n)
    def removeDuplicates2(self, nums: List[int]) -> int:
        l = 1
        for r in range(1, len(nums)):
            if nums[r] != nums[r - 1]:
                nums[l] = nums[r]
                l += 1
        return l

    # O(n)
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 1
        while r <= (len(nums) - 1):
            if nums[l] != nums[r]:
                l += 1
                r += 1
                continue
            if nums[l] == nums[r]:
                r += 1
                if r >= len(nums):
                    for i in range(1, (r - l)):
                        nums[l + i] = None
                    break
                while nums[l] == nums[r]:
                    r += 1
                    if r >= len(nums):
                        for i in range(1, (r - l)):
                            nums[l + i] = None
                        break
                if r <= (len(nums) - 1):
                    for i in range(1, (r - l)):
                        nums[l + i] = nums[r]
                    l = l + 1
                    r = l + 1

        return l + 1


if __name__ == "__main__":
    solution = Solution()
    solution.removeDuplicates(TEST)

def test_solution():
    solution = Solution()
    assert solution.removeDuplicates(TEST2) == 2
