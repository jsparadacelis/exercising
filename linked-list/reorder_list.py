from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # get the middle point
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # reverse second half
        second = slow.next
        prev = None
        slow.next = None
        while second:
            aux = second.next
            second.next = prev
            prev = second
            second = aux

        # merge lists
        first = head
        second = prev
        while second:
            aux1 = first.next
            aux2 = second.next
            first.next = second
            second.next = aux1
            first = aux1
            second = aux2
        



if __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    solution = Solution()
    solution.reorderList(head=head)
    print(head)
