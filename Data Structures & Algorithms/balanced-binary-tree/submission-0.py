# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool: 
        
        def rec(root): 
            if not root: return 0 
            lt = rec(root.left) 
            rt = rec(root.right) 
            if lt == -1 or rt == -1: 
                return -1 
            if abs(lt - rt) > 1: 
                return -1 
            return 1 + max(lt, rt) 
        return False if rec(root) == -1 else True
        