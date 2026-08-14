# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        l1 = list1
        l2 = list2
        while l1 and l2:
            v1 = l1.val 
            v2 = l2.val 
            if v1 <= v2 :
                current.next = ListNode(v1)
                l1 = l1.next
            else:
                current.next = ListNode(v2)
                l2 = l2.next

            current = current.next

        if l1:
            current.next = l1
        else:
            current.next = l2

        return dummy.next


