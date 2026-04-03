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
        tail: ListNode = None

        while cur_1 != None and cur_2 != None:
            self.print_linked_list(res)
            if cur_1.val < cur_2.val:
                if res == None:
                    new_node = ListNode(cur_1.val)
                    res = new_node
                    tail = res
                else :
                    new_node = ListNode(cur_1.val)
                    tail.next = new_node
                    tail = new_node

                cur_1 = cur_1.next
            elif cur_2.val < cur_1.val:
                if res == None:
                    new_node = ListNode(cur_2.val)
                    res = new_node
                    tail = res
                else :
                    new_node = ListNode(cur_2.val)
                    tail.next = new_node
                    tail = new_node

                cur_2 = cur_2.next
            else:
                if res == None:
                    new_head_node = ListNode(cur_1.val)
                    new_tail_node = ListNode(cur_2.val)
                    res = new_head_node
                    tail = new_tail_node
                    res.next = tail
                else:
                    new_node1 = ListNode(cur_1.val)
                    new_node2 = ListNode(cur_2.val)
                    tail.next = new_node1
                    tail = new_node1

                    tail.next = new_node2
                    tail = new_node2

                cur_1 = cur_1.next
                cur_2 = cur_2.next

        if cur_1:
            if res == None:
                res = cur_1
            else:
                tail.next = cur_1
                tail = cur_1
        elif cur_2:
            if res == None:
                res = cur_2
            else:
                tail.next = cur_2
                tail = cur_2

        return res

    def print_linked_list(self, head) -> None:
        cur = head
        arr = []

        while cur != None:
            arr.append(str(cur.val))
            cur = cur.next

        print(", ".join(arr))