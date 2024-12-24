# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = dummy.next

        while curr and curr.next:
            first = curr
            second = curr.next

            prev.next = second
            first.next = second.next
            second.next = first

            prev = first
            curr = first.next

        return dummy.next    
        