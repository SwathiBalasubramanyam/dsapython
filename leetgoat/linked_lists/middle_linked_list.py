# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node_len = 0
        tmp_head = head
        while tmp_head:
            node_len += 1
            tmp_head = tmp_head.next

        mid = (node_len//2) + 1

        node_len = 0
        while head:
            node_len += 1
            if node_len == mid:
                return head
            head = head.next

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow