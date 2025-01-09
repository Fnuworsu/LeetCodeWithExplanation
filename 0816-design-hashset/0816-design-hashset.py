class ListNode:
    def __init__(self, val=-1, next=None):
        self.val = val
        self.next = next

class MyHashSet:

    def __init__(self):
        self.hashSet = ListNode()

    def add(self, key: int) -> None:
        node = ListNode(key)
        curr = self.hashSet

        while curr.next:
            curr = curr.next

        curr.next = node    

    def remove(self, key: int) -> None:
        temp = ListNode()
        temp.next = self.hashSet
        curr = temp

        while curr.next:
            if curr.next.val == key:
                curr.next = curr.next.next
            else:
                curr = curr.next   

        self.hashSet = temp.next         

    def contains(self, key: int) -> bool:
        curr = self.hashSet

        while curr:
            if curr.val == key:
                return True
            curr = curr.next

        return False            
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)