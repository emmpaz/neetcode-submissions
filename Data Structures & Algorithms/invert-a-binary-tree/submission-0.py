# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        #check if there is a root
        #recursion
        #right = rec(left)
        #left = rec(right)
        #
        def rec(node):
            
            if node == None:
                return node

            tmp = node.right
            node.right = rec(node.left)
            node.left = rec(tmp)

            return node
        
        return rec(root)


        