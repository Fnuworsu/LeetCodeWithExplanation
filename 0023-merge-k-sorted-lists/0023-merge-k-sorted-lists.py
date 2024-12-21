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
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = PriorityQueue()

        for l in lists:
            if l: pq.put(Wrapper(l))

        ret = res = ListNode()

        while not pq.empty():
            node = pq.get().node
            res.next = node
            res = res.next
            node = node.next

            if node: pq.put(Wrapper(node))

        return ret.next        


        