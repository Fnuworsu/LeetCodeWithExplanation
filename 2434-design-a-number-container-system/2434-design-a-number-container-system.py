from sortedcontainers import SortedDict, SortedList

class NumberContainers:

    def __init__(self):
        self.nums = defaultdict(lambda: SortedList()) #n -> idx
        self.index = {} # idx -> n

    def change(self, index: int, number: int) -> None:
        if index in self.index:
            oldNum = self.index[index]
            # self.index[index] = number
            self.nums[oldNum].discard(index)

        self.nums[number].add(index)
        self.index[index] = number

    def find(self, number: int) -> int:
        if number in self.nums and self.nums[number]:
            return self.nums[number][0] 
        
        return -1


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
"""
nums = {
    10 : (2,3,5)
    20 : 1
}

index = {
    1 : 20
    2 : 10
    3 : 10
    5 : 10
}
"""