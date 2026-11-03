# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = ListNode(0,head)
        # cur = head
        # ref = dummy

        # while cur.next:
        #     if cur.next.val and cur.val == cur.next.val:
        #         while cur.next.val and cur.val == cur.next.val:
        #             cur = cur.next
        #         ref.next = cur.next 
        #     else:
        #          ref = ref.next  

        #     cur = cur.next

        # return dummy.next
        if not head:
            return None

        dummy = ListNode(0,head)
        list_builder = dummy
        cur = head

        while cur:
            dup=False
            while cur.next and cur.val == cur.next.val:
                dup=True
                cur = cur.next
            if not dup:
                list_builder.next = cur
                list_builder=cur
            cur=cur.next

        if dup:
            list_builder.next = None
        
        return dummy.next

            
    












