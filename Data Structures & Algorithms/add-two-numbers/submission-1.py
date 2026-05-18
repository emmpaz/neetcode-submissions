# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # lists will always have items
        # list contain only positive numbers
        # different length

        dummy = ListNode()
        tail = dummy
        ptr1 = l1   
        ptr2 = l2
        carry = 0

        while ptr1 and ptr2:
            val1 = ptr1.val
            val2 = ptr2.val

            remainder = (carry + val1 + val2) % 10
            tail.next = ListNode(remainder)
            tail = tail.next

            carry = (val1 + val2) // 10

            ptr1 = ptr1.next
            ptr2 = ptr2.next

        if ptr1:
            while ptr1:
                val1 = ptr1.val

                remainder = (carry + val1) % 10
                tail.next = ListNode(remainder)
                tail = tail.next

                carry = (val1 + carry) // 10

                ptr1 = ptr1.next
        else:
            while ptr2:
                val2 = ptr2.val

                remainder = (carry + val2) % 10
                tail.next = ListNode(remainder)
                tail = tail.next

                carry = (val2 + carry) // 10

                ptr2 = ptr2.next

        if carry:
            tail.next = ListNode(carry)

        return dummy.next            
            