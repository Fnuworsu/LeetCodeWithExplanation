class Allocator:

    def __init__(self, n: int):
        self.mem = [0 for _ in range(n)]
        self.memAddress = defaultdict(list)

    def allocate(self, size: int, mID: int) -> int:
        """
        freespace == size
        startIdx
        """
        startIdx = -1
        freeSpace = 0

        for i in range(len(self.mem)):
            if self.mem[i] == 0:
                if startIdx == -1:
                    startIdx = i
                
                freeSpace += 1
                if freeSpace == size:
                    break
            else:
                freeSpace = 0
                startIdx = -1
            
        
        if startIdx < 0 or freeSpace != size:
            return -1

        for i in range(startIdx, startIdx + size):
            self.mem[i] = mID
            self.memAddress[mID].append(i)
        
        return startIdx

    def freeMemory(self, mID: int) -> int:
        freed = len(self.memAddress[mID])

        if not freed:
            return 0

        for idx in self.memAddress[mID]:
            self.mem[idx] = 0
        
        del self.memAddress[mID]

        return freed


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.freeMemory(mID)