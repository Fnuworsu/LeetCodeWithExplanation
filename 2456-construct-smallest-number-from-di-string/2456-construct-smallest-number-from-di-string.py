class Solution:
    def smallestNumber(self, pattern: str) -> str:
        minNum = float('inf')
        used = [0] * 10
        n = len(pattern)

        def back(idx, start, end, path):
            nonlocal minNum
            #base case
            if len(path) == n+1:
                minNum = min(minNum, int("".join(path[:])))
                return
            
            for i in range(start, end+1):
                if used[i]:
                    continue
                
                path.append(str(i))
                used[i] = 1

                if idx < n:
                    if pattern[idx] == "I":
                        back(idx+1, i+1, 9, path)
                    else:
                        back(idx+1, 1, i-1, path)
                else:
                    back(idx+1, -1, -1, path)
                
                path.pop()
                used[i] = 0
        
        back(0, 1, 9, [])

        return str(minNum)