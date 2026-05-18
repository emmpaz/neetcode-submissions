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

        ptr = head

        while ptr:
            temp = ptr.next

            ptr.next = Node(ptr.val, temp)

            ptr = temp
        
        ptr = head
        while ptr:
            ptr.next.random = ptr.random.next if ptr.random else None

            ptr = ptr.next.next

        dummy = Node(0)
        tail = dummy
        ptr = head

        while ptr:
            tail.next = ptr.next
            tail = tail.next

            ptr.next = ptr.next.next
            ptr = ptr.next
        
        return dummy.next

