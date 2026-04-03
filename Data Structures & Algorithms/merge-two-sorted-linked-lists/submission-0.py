# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur_1 = list1
        cur_2 = list2
        res: ListNode = None

        while cur_1 != None and cur_2 != None:
            self.print_linked_list(res)
            if cur_1.val < cur_2.val:
                res = self.add(res, ListNode(cur_1.val))
                cur_1 = cur_1.next
            elif cur_2.val < cur_1.val:
                res = self.add(res, ListNode(cur_2.val))
                cur_2 = cur_2.next
            else:
                res = self.add(res, ListNode(cur_1.val))
                res = self.add(res, ListNode(cur_2.val))
                cur_1 = cur_1.next
                cur_2 = cur_2.next

        if cur_1:
            res = self.add(res, cur_1)
        elif cur_2:
            res = self.add(res, cur_2)

        return res

    
    def add(self, head, new_node):
        cur = head

        if not head:
            head: ListNode = new_node
            return head

        while cur.next != None:
            cur = cur.next

        cur.next = new_node
        return head

    def print_linked_list(self, head) -> None:
        cur = head
        arr = []

        while cur != None:
            arr.append(str(cur.val))
            cur = cur.next

        print(", ".join(arr))