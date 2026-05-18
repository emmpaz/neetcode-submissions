# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        md = 0

        def rec(root):
            if not root: return 0

            dl = rec(root.left)
            dr = rec(root.right)

            nonlocal md
            md = max(md, dl + dr)

            return 1 + max(dr, dl)
        
        rec(root)
        return md