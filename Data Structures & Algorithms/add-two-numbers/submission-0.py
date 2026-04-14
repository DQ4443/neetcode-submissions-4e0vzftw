# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # iterate a ptr though both lists.
        # add node.val into res list node. 
        # if > 9, set carry to true
        # check carry true to add 1

        new = ListNode(-1, None)
        anchor = new

        ptr1, ptr2 = l1, l2

        carry = False

        while ptr1 or ptr2:
            psum = 0
            if ptr1:
                psum += ptr1.val
                ptr1 = ptr1.next
            if ptr2:
                psum += ptr2.val
                ptr2 = ptr2.next
            if carry == True:
                psum += 1

            if psum >= 10:
                carry = True
                psum -= 10
            else:
                carry = False

            new.next = ListNode(psum, None)
            new = new.next

            print(anchor.next.val)

        if carry == True:
            new.next = ListNode(1, None)
        return anchor.next
