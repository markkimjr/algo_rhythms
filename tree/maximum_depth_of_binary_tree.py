"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Example:
Input: root = [3,9,20,null,null,15,7]
Output: 3
"""
from collections import deque
from typing import Optional



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        stack = [[root, 1]]
        res = 0

        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return res



if __name__ == "__main__":
    solution = Solution()
    tree_node1 = TreeNode()
    tree_node2 = TreeNode()
    tree_node = TreeNode(val=0, left=tree_node1, right=tree_node2)
    solution.maxDepth(tree_node)
