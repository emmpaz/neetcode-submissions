# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next == None or head.next.next == None:
            return None

        fast = head
        slow = head
        prev = None

        while fast != None and fast.next != None:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        
        middle = slow
        prev.next = None

        #reverse second list
        dummy = None

        while middle != None:
            tmp = middle.next

            middle.next = dummy
            dummy = middle
            middle = tmp
        
        list1 = head
        list2 = dummy

        while list1 and list2:
            next1 = list1.next
            next2 = list2.next

            list1.next = list2
            if next1:
                list2.next = next1
            
            list1 = next1
            list2 = next2
        



