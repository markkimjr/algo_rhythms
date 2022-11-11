"""
Given the head of a singly linked list, reverse the list, and return the reversed list.

Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
"""

TEST = [1, 2, 3, 4, 5]


# TODO review
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# O(n)
def reverse_list(head: ListNode) -> ListNode:
    prev = None

    while head:
        nxt = head.next
        head.next = prev
        prev = head
        head = nxt
    return prev



if __name__ == "__main__":
    dummy5 = ListNode(val=5)
    dummy4 = ListNode(val=4, next=dummy5)
    dummy3 = ListNode(val=3, next=dummy4)
    dummy2 = ListNode(val=2, next=dummy3)
    dummy_head = ListNode(val=1, next=dummy2)

    reverse_list(dummy_head)
