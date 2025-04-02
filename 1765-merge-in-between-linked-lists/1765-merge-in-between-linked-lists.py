# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        node = list1

        for _ in range(a-1):
            node = node.next
        
        temp = node.next

        for _ in range(b-a):
            temp = temp.next
        # print(temp.val)
        
        node.next = list2

        while node.next:
            node = node.next
        
        node.next = temp.next

        return list1