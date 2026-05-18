# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # we store the lowest common ancestor
        # we start it at the root

        def rec(root):
            if not root:
                return None
            
            l = rec(root.left)
            r = rec(root.right)
            
            if l and r:
                return root
            if (l or r) and (root.val == p.val or root.val == q.val):
                return root
            if (root.val == p.val or root.val == q.val):
                return root

            if l: return l
            if r: return r

            return None

        return rec(root)
            

