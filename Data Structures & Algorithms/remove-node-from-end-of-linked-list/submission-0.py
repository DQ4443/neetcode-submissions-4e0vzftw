# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # need to anchor head with sent
        # send 1 ptr to find length of list
        # iterate a pointer until nth node from end
        # update relevant pointers
        # return sent.next

        sent = ListNode(-1, head)
        
        temp = head
        L = 0
        while temp:
            temp = temp.next
            L += 1

        print(L)

        # node to update = L - n

        temp2 = sent
        num = 0
        while num < L - n and temp2:
            temp2 = temp2.next
            n += 1

        print(temp2.val)

        temp2.next = temp2.next.next

        return sent.next