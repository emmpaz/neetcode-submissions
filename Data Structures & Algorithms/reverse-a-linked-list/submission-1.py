# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        dummy = None
        tmp = head

        while tmp:
            hold = tmp.next
            tmp.next = dummy

            dummy = tmp
            tmp = hold

        return dummy