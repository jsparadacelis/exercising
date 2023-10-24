from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = ListNode()
        curr = dummy

        tail = ListNode()
        head = tail
        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        return dummy.next


if __name__ == "__main__":

    solution = Solution()
    list1 = ListNode(1, ListNode(3, ListNode(5)))
    list2 = ListNode(2, ListNode(3, ListNode(7, ListNode(8))))
    solution.mergeTwoLists(list1=list1, list2=list2)
