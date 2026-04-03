# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # 1 -> 2 -> 3

    # 2 -> 3

    # 3 -> 

    # new_node = 3 -> 2

    #

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        new_node = self.reverseList(head.next)

        cur = new_node
        while cur.next != None:
            cur = cur.next

        cur.next = head

        head.next = None

        return new_node
        