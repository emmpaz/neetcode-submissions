# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        

        def rec(root, greatestValue):
            if not root: return 0
            

            l = rec(root.left, max(greatestValue, root.val))
            r = rec(root.right, max(greatestValue, root.val))

            if root.val >= greatestValue:
                return 1 + l + r
            else:
                return l + r
        
        return rec(root, root.val)