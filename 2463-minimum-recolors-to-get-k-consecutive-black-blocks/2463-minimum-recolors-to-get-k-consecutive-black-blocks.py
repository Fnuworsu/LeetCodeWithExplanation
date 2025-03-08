class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        curr = 0

        for i in range(k):
            if blocks[i] == "W":
                curr += 1
        
        minOps = curr
        l = 0

        for r in range(k, len(blocks)):
            if blocks[l] == "W":
                minOps -= 1
            if blocks[r] == "W":
                minOps += 1
            
            curr = min(curr, minOps)
            l += 1
        
        return curr

        