# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# https://leetcode.com/problems/balanced-binary-tree/
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def get_max_depth(node):
            if not node:
                return 0

            left_val = get_max_depth(node.left)
            right_val = get_max_depth(node.right)

            if left_val == -1 or right_val == -1 or abs(left_val - right_val) > 1:
                return -1

            return 1 + max(left_val, right_val)

        return True if get_max_depth(root) != -1 else False

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# https://leetcode.com/problems/remove-linked-list-elements/
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        dummyNode = ListNode()
        root = dummyNode

        while head:
            if head.val != val:
                root.next = head
                root = root.next
            else:
                root.next = None
            head = head.next
        return dummyNode.next
    
# https://leetcode.com/problems/reverse-linked-list/
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyNode = None
        root = dummyNode

        while head:
            curr_next = head.next

            head.next = root
            root = head
            head = curr_next

        return root

# https://leetcode.com/problems/middle-of-the-linked-list/description/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    import math
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # slow = fast  = head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next

        # return slow
        
        # len = 0
        # curr = head
        # while curr:
        #     len += 1
        #     curr = curr.next

        # mid = math.floor((len/2) + 1)
        
        # curr_idx = 1
        # curr_node = head
        # while curr_idx != mid:
        #     curr_node = curr_node.next
        #     curr_idx += 1

        # return curr_node

        def find_mid(slow, fast):
            if not fast or not fast.next:
                return slow

            return find_mid(slow.next, fast.next.next)

        return find_mid(head, head)
        

            