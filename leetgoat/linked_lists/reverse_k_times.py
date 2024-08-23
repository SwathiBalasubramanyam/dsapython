# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        res_head = ListNode()
        res_tail = res_head
        while head:
            tmp_head = ListNode()
            tmp_tail = tmp_head
            node_cnt = 0
            while head and node_cnt < k:
                tmp_tail.next = ListNode(head.val)
                tmp_tail = tmp_tail.next
                head = head.next
                node_cnt += 1

            res_tail.next = self.reverse(tmp_head.next) if node_cnt == k else tmp_head.next
            for i in range(k):
                if res_tail:
                    res_tail = res_tail.next
                else:
                    break
            
        return res_head.next


    def reverse(self, head):
        prev_node = None
        while head:
            next_node = head.next
            head.next = prev_node
            prev_node = head
            head = next_node

        return prev_node


    