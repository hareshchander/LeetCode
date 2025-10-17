# https://www.youtube.com/watch?v=rxoDDt3RCOs
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr, prev = head, None

        while curr:
            Next = curr.next     # stored in Next for future use
            curr.next = prev # This curr.next is the tail or connecting node so prev moved here
            prev = curr          
            curr = Next          #  Stored Next is used here

        return prev


# We redirect the next pointer of curr to point backward to the reversed part.

# Before: 1 -> 2

# After: 1 -> None (because prev is currently None)

# \U0001f4a1 Think of it as “flip the arrow of this node to point to the previous node.”

        






