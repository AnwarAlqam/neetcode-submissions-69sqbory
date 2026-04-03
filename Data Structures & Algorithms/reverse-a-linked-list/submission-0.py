# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        res: ListNode = None
        while cur != None:
            if res == None:
                res = ListNode(cur.val)
            else:
                new_head = ListNode(cur.val)
                new_head.next = res
                res = new_head

            cur = cur.next

        return res

            
            