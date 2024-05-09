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
        old_head = head
        root = head
        while root.next:
            root = root.next
            ll_len += 1

        old_tail = root
            
        k %= ll_len
        if not k:
            return head
            
        new_tail_pos = ll_len-k-1
        new_tail = head
        while new_tail_pos:
                new_tail = new_tail.next
                new_tail_pos -= 1

        new_head = new_tail.next
        new_tail.next = None
        old_tail.next = old_head

        return new_head
        