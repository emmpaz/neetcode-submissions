# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # we can create 2 functions 
        # one is checking if the tree exists in the other one

        def checkTree(r1, r2):
            if not r1 and not r2:
                return True
            if (r1 and not r2) or (r2 and not r1):
                return False
            if r1.val != r2.val:
                return False
            
            l = checkTree(r1.left, r2.left)
            r = checkTree(r1.right, r2.right)

            return l and r

        if not root:
            return False
        
        check = checkTree(root, subRoot)

        if check:
            return True
        
        l = self.isSubtree(root.left, subRoot)
        r = self.isSubtree(root.right, subRoot)

        return l or r

                
