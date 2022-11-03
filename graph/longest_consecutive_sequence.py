"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
"""
from typing import List

TEST = [100, 4, 200, 1, 3, 2]


class Solution:
    # O(n) using set
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0
        for num in nums:
            if (num - 1) not in num_set:
                length = 0
                while num + length in num_set:
                    length += 1
                if length > longest:
                    longest = length
        return longest

    # using sort to solve problem O(nlogn)
    def longestConsecutiveSorting(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        longest = 1
        current = 1
        for l in range(len(nums)):
            if l == (len(nums) - 1):
                break
            if nums[l] == nums[l + 1]:
                continue
            if nums[l + 1] - nums[l] == 1:
                current += 1
                longest = max(longest, current)
                continue
            longest = max(longest, current)
            current = 1

        return longest


def test_longest_consecutive():
    solution = Solution()
    assert solution.longestConsecutiveSorting(TEST) == 4


if __name__ == "__main__":
    solution = Solution()
    solution.longestConsecutiveSorting(TEST)
