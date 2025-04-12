class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.count = 0
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self, arr):
        self.cache = {'a', 'e', 'i', 'o', 'u'}
        self.root = self.build(arr, 0, len(arr)-1)

    def build(self, arr, start, end):
        if start > end:
            return None
        
        node = Node(start, end)

        if start == end:
            node.count = 1 if (arr[start][0] in self.cache and arr[start][-1] in self.cache) else 0
            return node

        mid = (start + end) // 2
        node.left = self.build(arr, start, mid)
        node.right = self.build(arr, mid+1, end)
        node.count = node.left.count + node.right.count

        return node
    
    def query(self, node, l, r):
        if not node or l > node.end or r < node.start:
            return 0
        
        if l <= node.start and r >= node.end:
            return node.count
        
        left = self.query(node.left, l, r)
        right = self.query(node.right, l, r)

        return left + right

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ST = SegmentTree(words)
        res = []

        for l,r in queries:
            res.append(ST.query(ST.root, l, r))
        
        return res
"""
space = O(n) for segment tree
time complexity = 0(n) to build segmentree, O(klog(n)) for all queries
"""