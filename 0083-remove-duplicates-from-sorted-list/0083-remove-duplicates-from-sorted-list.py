# https://www.youtube.com/watch?v=mKm3AmKTap0
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head

        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next  
                # This indicates that now currents's next is the curr.next.next

            else:
                curr = curr.next     # This only points the curr.next node.

        return head













       