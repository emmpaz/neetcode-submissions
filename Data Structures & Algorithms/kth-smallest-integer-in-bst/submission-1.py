# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:


        def rec(root, curr):

            if not root: return (None, curr)

            ln, curr = rec(root.left, curr)
            if ln: return (ln, curr)

            curr += 1
            if curr == k:
                return (root, curr)
            
            rn, curr = rec(root.right, curr)
            if rn: return (rn, curr)

            return (None, curr)
        
        node, curr = rec(root, 0)

        return node.val