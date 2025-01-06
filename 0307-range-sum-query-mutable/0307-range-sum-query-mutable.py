class Node:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.sum = 0
        self.left = None
        self.right = None

class SegmentTree:
    def __init__(self, arr):
        self.root = self.build(arr, 0, len(arr)-1)
        
    def build(self, arr, start, end):
        if start > end:
            return None
        node = Node(start, end)
        if start == end:
            node.sum = arr[start]
            return node
        mid = (start + end) // 2
        
        node.left = self.build(arr, start, mid)
        node.right = self.build(arr, mid+1, end)
        
        node.sum = node.left.sum + node.right.sum
        return node
    
    def query(self, node, l, r):
        if not node or l > node.end or r < node.start:
            return 0
        if l <= node.start and r >= node.end:
            return node.sum
            
        leftSum = self.query(node.left, l, r)
        rightSum = self.query(node.right, l, r)
        
        return leftSum + rightSum
    
    def update(self, node, idx, value):
        if not node or idx < node.start or idx > node.end:
            return
        if node.start == node.end:
            node.sum = value
            return
        self.update(node.left, idx, value)
        self.update(node.right, idx, value)
        
        node.sum = node.left.sum + node.right.sum

class NumArray:

    def __init__(self, nums: List[int]):
        self.st = SegmentTree(nums)

    def update(self, index: int, val: int) -> None:
        self.st.update(self.st.root, index, val)
        

    def sumRange(self, left: int, right: int) -> int:
        return self.st.query(self.st.root, left, right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)