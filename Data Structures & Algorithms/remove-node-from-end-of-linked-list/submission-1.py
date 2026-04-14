# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # move ptr to end to find L
        # move ptr to L - n, then update
        # use sent to keep trak of head

        sent = ListNode(-1, head)

        ptr1 = sent
        L = -1
        while ptr1:
            ptr1 = ptr1.next
            L += 1

        print(L)

        ptr2 = sent
        num = 0
        while num < L - n:
            ptr2 = ptr2.next
            num += 1

        print(ptr2.val)
        ptr2.next = ptr2.next.next

        return sent.next