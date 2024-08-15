# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        tmp_head = head
        length = 0
        while tmp_head:
            length += 1
            tmp_head = tmp_head.next

        new_head = ListNode()
        tail = new_head
        node_cnt = 0
        node_to_delete = length-n+1

        while head:
            node_cnt += 1
            if node_to_delete != node_cnt:
                tail.next = ListNode(head.val)
                tail = tail.next

            head = head.next
        return new_head.next
            
