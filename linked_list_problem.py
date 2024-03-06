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

        