"""
Given the root of a binary tree, invert the tree, and return its root.

Example
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def _init__(self):
        pass

    # O(n)
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        left = root.left
        right = root.right
        root.left = right
        root.right = left

        self.invertTree(left)
        self.invertTree(right)

        return root

