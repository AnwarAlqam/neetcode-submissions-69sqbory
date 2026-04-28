# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        if n == 1:
            return head.next

        cur = head
        prev = None
        i = 0
        while cur != None:
            if i == n:
                prev.next = cur.next
                break

            prev = cur
            cur = cur.next
            i += 1
        return head