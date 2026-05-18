# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        
        if not root: return []
        ml = []

        def rec(root, depth, mainList):

            if not root: return mainList

            if len(ml) - 1 < depth:
                mainList.append(root.val)

            r = rec(root.right, depth + 1, mainList)
            l = rec(root.left, depth + 1, mainList)

            return mainList
        
        return rec(root, 0, ml)