"""
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
"""

TEST = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

OUTPUT = [1, 10, 2, 9, 3, 8, 4, 7, 5, 6]

OUTPUT2 = [1, 11, 2, 10, 3, 9, 4, 8, 5, 7, 6]


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def __init__(self):
        pass

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        hashmap = {}

        counter = 0
        init = head

        while init:
            hashmap[counter] = init
            init = init.next
            counter += 1

        length = len(hashmap.keys())
        left = head
        right = hashmap[max(hashmap.keys())]

        while left != right:
            tmp_left = left
            tmp_right = right
            left.next = right
            right.next = left.next.next
            left = left.next
            right = hashmap[length - 1]


