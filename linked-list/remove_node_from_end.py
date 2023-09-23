from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        container = []
        while head:
            container.append(head)
            head = head.next
        
        result = tail = ListNode()
        for idx, node in enumerate(container):
            if len(container) - n == idx:
                continue
            tail.next = ListNode(val=node.val)
            tail = tail.next
        return result.next


if  __name__ == '__main__':
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    solution = Solution()
    result = solution.removeNthFromEnd(head=head, n=2)
