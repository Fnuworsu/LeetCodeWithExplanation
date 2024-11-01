# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        [1,2,3,4,5]
        prev = None
        node = head

        temp = [2,3,4,5]
        node.next = prev (node = [1, None])
        prev = node ([1,None])
        node = temp [2,3,4,5]

        temp = [3,4,5]
        node.next = [1,None]
        prev = [2,1, None]
        node = [3,4,5]

        temp = [4,5]
        node.next = [2,1,None]
        prev = [3,2,1,None]
        node =[4, 5]

        temp = [5]
        node.next = [3,2,1,None]
        prev = [4,3,2,1,None]
        node = [5]

        temp = [None]
        node.next = [4,2,3,2,1,None]
        prev = [5,4,3,2,1,None]
        node = None

        Loop ends when node is None

        """
        prev, node = None, head

        while node:
            temp = node.next
            node.next = prev
            prev = node
            node = temp

        return prev    
        