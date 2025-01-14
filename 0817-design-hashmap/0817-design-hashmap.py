class ListNode:
    def __init__(self, val, key):
        self.val = val
        self.key = key

class MyHashMap:

    def __init__(self):
        self.size = 10**6 + 7
        self.acc = [0] * self.size
    
    def idx(self, key):
        return key % self.size

    def put(self, key: int, value: int) -> None:
        i = self.idx(key)
        node = ListNode(value, key)
        self.acc[key] = node

    def get(self, key: int) -> int:
        i = self.idx(key)

        if self.acc[key] == 0:
            return -1
        return self.acc[key].val     

    def remove(self, key: int) -> None:
        i = self.idx(key)
        self.acc[key] = 0
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)