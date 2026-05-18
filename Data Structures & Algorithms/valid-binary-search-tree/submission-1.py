# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # this is like finding the "good" nodes
        # but we need to keep track of the root node's val
        # because all nodes on the left need to be less than the root
        # and all right nodes need to be greater than the root

        def rec(root, upper, lower):

            if not root: return True

            if not root.val > lower or not root.val < upper:
                return False
            
            l = rec(root.left, root.val, lower)
            r = rec(root.right, upper, root.val)

            return l and r
        
        return rec(root,  float('inf'), float('-inf'))