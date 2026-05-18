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
        tmp2 = head.next

        while tmp:
            tmp.next = dummy

            dummy = tmp
            tmp = tmp2
            tmp2 = tmp2.next if tmp2 else None

        return dummy