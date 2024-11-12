# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        A, B = headA, headB
        lA, lB = 0, 0
        
        node = A
        while node:
            lA += 1
            node = node.next

        node = B
        while node:
            lB += 1
            node = node.next

        diff = abs(lA - lB)

        if lA > lB:
            while diff > 0:
                A = A.next
                diff -= 1
        else:
            while diff > 0:
                B = B.next
                diff -= 1

        while A and B:
            if A == B:
                return A
            A = A.next
            B = B.next

        return None                                
        