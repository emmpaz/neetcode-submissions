# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        


        def rec(curr, root):

            if not root: return (curr, None)

            curr, ln = rec(curr, root.left)

            if ln: return (curr, ln)
            
            curr += 1
            if curr == k:
                return (curr, root)

            curr, rn = rec(curr, root.right)
            if rn: return (curr, rn)

            return (curr, None)
        
        curr, node = rec(0, root)
        return node.val
            

