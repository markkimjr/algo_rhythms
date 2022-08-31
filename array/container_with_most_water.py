"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
"""

test_case = [1, 8, 6, 2, 5, 4, 8, 3, 7]

# brute force On^2
def get_max_area(nums: list) -> int:
    max_area = 0
    for l in range(len(nums)):
        for r in range(l + 1, len(nums)):
            area = (r - l) * min(nums[l], nums[r])
            if area > max_area:
                max_area = area

    return max_area


# O(n)
def get_max_area_efficiently(nums: list) -> int:
    max_area = 0
    l = 0
    r = len(nums) - 1
    while l < r:
        area = (r - l) * min(nums[l], nums[r])
        if area > max_area:
            max_area = area

        if nums[l] < nums[r]:
            l += 1
        else:
            r -= 1

    return max_area



def test_solution():
    assert get_max_area(test_case) == 49

