# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # keep track of depth for each node
        # parameter possibly
        # pass the entire parent list aswell

        if not root: return []
        ml = []

        def rec(root, depth, mainList):

            if not root: return mainList

            if len(mainList) - 1 >= depth:
                mainList[depth].append(root.val)
            
            if len(mainList) - 1 < depth:
                nl = []
                nl.append(root.val)
                mainList.append(nl)
            
            l = rec(root.left, depth+1, mainList)
            r = rec(root.right, depth+1, mainList)

            return mainList
        
        return rec(root, 0, ml)
            