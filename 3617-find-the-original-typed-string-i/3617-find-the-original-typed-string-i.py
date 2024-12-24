class Solution:
    def possibleStringCount(self, word: str) -> int:
        resMap = defaultdict(int)
        stack = []
        i = 0

        for c in word:
            if stack and stack[-1] != c:
                print(stack," => check")
                if len(stack) > 1:
                    k = stack[-1]
                    if k in resMap:
                        resMap[(k,i)] = len(stack)
                        i += 1
                    else:
                        resMap[k] = len(stack)
                stack = [c]
            else:
                stack.append(c)
                print(stack, " => add")

        if stack and list(set(stack))[0] == stack[-1]:
            k = stack[-1]
            if k in resMap:
                resMap[(k,i)] = len(stack)
                i += 1
            else:
                resMap[k] = len(stack)    
               

        res = 1

        for v in resMap.values():
            res += (v-1)

        return res                    
        