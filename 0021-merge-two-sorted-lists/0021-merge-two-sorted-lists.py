# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Wrapper:
    def __init__(self, node):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        heap = []
        
        if list1: heapq.heappush(heap, Wrapper(list1))
        if list2: heapq.heappush(heap, Wrapper(list2))

        ret = res = ListNode()

        while heap:
            wrapper = heapq.heappop(heap)
            node = wrapper.node
            res.next = node
            res = res.next
            node = node.next

            if node:
                heapq.heappush(heap, Wrapper(node))

        return ret.next        
        