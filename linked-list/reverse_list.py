# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        reversed = None
        while head:
            aux = reversed
            reversed = head
            head = head.next
            reversed.next = aux

        return reversed

if __name__ == "__main__":
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    solution = Solution()
    solution.reverseList(head=head)