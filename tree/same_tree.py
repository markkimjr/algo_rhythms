"""
Given the roots of two binary trees p and q, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Example
Input: p = [1,2,3], q = [1,2,3]
Output: true
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        pass

    # O(p + q)
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_nodes = [p]
        q_nodes = [q]

        while p_nodes and q_nodes:
            p = p_nodes.pop()
            q = q_nodes.pop()

            if p and q:
                if p.val != q.val:
                    return False
                p_nodes.append(p.left)
                p_nodes.append(p.right)
                q_nodes.append(q.left)
                q_nodes.append(q.right)
            else:
                if p and not q:
                    return False
                if q and not p:
                    return False

        return True

    # DFS - O(p + q)
    def isSameTree2(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and q:
            if p.val != q.val:
                return False
        if p and not q:
            return False
        if q and not p:
            return False
        if not p and not q:
            return True

        left_true = self.isSameTree2(p.left, q.left)
        right_true = self.isSameTree2(p.right, q.right)

        return True if left_true and right_true else False


if __name__ == "__main__":
    solution = Solution()
    tree_node1 = TreeNode()
    tree_node2 = TreeNode(val=2, left=None, right=None)
    tree_node = TreeNode(val=0, left=tree_node1, right=tree_node2)

    tree_node1f = TreeNode()
    tree_node2f = TreeNode(val=1, left=None, right=None)
    tree_nodef = TreeNode(val=0, left=tree_node1f, right=tree_node2f)
    solution.isSameTree2(tree_node, tree_nodef)