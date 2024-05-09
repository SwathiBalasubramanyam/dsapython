# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not k or not head or not head.next:
            return head

        ll_len = 1
        root = head
        tail = None
        while root.next:
            root = root.next
            ll_len += 1
            if not root.next:
                tail = root
            
        k %= ll_len
        if not k:
            return head
            
        tail_idx = ll_len - k

        old_head = head

        i = 1
        while i <= tail_idx:
            if i == tail_idx:
                node = head
                head = head.next
                node.next = None
            else:
                head = head.next
            i += 1

        tail.next = old_head

        return head
        