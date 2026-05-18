"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if head == None:
            return head
        # the random pointer may point to a node or null
        # deep copy list meaning all new nodes
        # maybe hm
        # 3 7 4 5
        # 3' 7' 4' 5'

        #first create the copies and store them
        hm = {}
        ptr = head

        while ptr:
            hm[ptr] = Node(ptr.val)
            ptr = ptr.next
        
        ptr = head

        while ptr:
            if ptr.next:
                hm[ptr].next = hm[ptr.next]
            
            if ptr.random:
                hm[ptr].random = hm[ptr.random]
            ptr = ptr.next
        
        return hm[head]


        
