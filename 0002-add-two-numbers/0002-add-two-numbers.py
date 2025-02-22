# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        2 -> 4 -> 3
        5 -> 6 -> 4

        node = (a+b) % 10
        carry = (a+b) // 10
        """
        node = ListNode()
        curr = node
        carry = 0

        while l1 or l2 or carry:
            x,y = 0,0

            if l1:
                x = l1.val
                l1 = l1.next
            
            if l2:
                y = l2.val
                l2 = l2.next
            
            val = (carry + x + y)
            carry = val // 10
            
            curr.next = ListNode(val % 10)
            curr = curr.next
        
        return node.next

        