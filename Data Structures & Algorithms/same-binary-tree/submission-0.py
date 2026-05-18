# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def rec(r1, r2):
            if not r1 and not r2:
                return True
            if (r1 and not r2) or (not r1 and r2):
                return False
            if r1.val != r2.val:
                return False

            l = rec(r1.left, r2.left)
            r = rec(r1.right, r2.right)

            return l and r
        
        return rec(p, q)


            