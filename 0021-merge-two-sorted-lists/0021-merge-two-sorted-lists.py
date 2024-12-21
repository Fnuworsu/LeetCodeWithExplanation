# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from queue import PriorityQueue

class Wrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        pq = PriorityQueue()

        if list1: pq.put(Wrapper(list1))
        if list2: pq.put(Wrapper(list2))

        ret = res = ListNode()

        while not pq.empty():
            node = pq.get().node
            res.next = node
            res = res.next
            node = node.next

            if node: pq.put(Wrapper(node))

        return ret.next    
              
        