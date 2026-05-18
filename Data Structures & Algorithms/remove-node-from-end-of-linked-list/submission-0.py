# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # so we have n that shows the distance from the end 
        # so essentially n-1 is the node to delete
        end = head

        for i in range(n-1):
            end = end.next
        
        prev = None
        target = head
        while end.next != None:
            prev = target
            target = target.next
            end = end.next

        if target == head:
            return target.next
        else:
            prev.next = target.next
        
        return head

        

