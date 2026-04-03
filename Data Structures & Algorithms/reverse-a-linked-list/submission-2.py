# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        new_node = self.reverseList(head.next)

        # Add it at the end of the list
        head.next.next = head
        head.next = None

        return new_node
        