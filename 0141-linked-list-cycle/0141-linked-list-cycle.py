# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:      
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False
        

        # Set = set()
        # current = head

        # while current:
        #     if current in Set:
        #         return True

        #     else:
        #         Set.add(current)

        #     current = current.next

        # return False

