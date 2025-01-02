# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        def getLen(node):
            curr, l = node, 0

            while curr:
                l += 1
                curr = curr.next

            return l

        k, i = getLen(head) - n, 0
        temp = ListNode
        temp.next = head
        curr = temp

        while curr.next:
            if i == k:
                curr.next = curr.next.next
                break

            curr = curr.next
            i += 1

        return temp.next        




        