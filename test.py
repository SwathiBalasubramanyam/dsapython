# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:


        def _dfs(node):
            if not node:
                return
            nonlocal curr
            _dfs(node.left)

            node.left = None
            curr.right = node
            curr = curr.right
            print("what is current", curr.val)
            _dfs(node.right)
            return

        dummy = TreeNode()
        curr = dummy
        _dfs(root)
        return dummy.right
    

    
resNode = Solution().increasingBST(TreeNode(5, TreeNode(1), TreeNode(7)))

while resNode:
    print(resNode.left, resNode.val, resNode.right)
    resNode = resNode.right
