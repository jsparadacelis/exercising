from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __lt__(self, other: __build_class__):
        return self.val < other.val
        


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        

        dummy = ListNode()
        head = tail
        while list1 and list2:

            if list1.val < list2.val:
                dummy.next = list1
                list1 = list1.next
            else:
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        
        if list1:
            dummy.next = list1
        elif list2:
            dummy.next = list2
        return head.next


if __name__ == "__main__":
    list1 = ListNode(2, ListNode(5, ListNode(7)))
    list2 = ListNode(3, ListNode(11))
    solution = Solution()
    solution.mergeTwoLists(list1=list1, list2=list2)
