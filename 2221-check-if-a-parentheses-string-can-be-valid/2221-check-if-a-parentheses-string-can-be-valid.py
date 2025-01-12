class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        if len(s) % 2 == 1:
            return False
        
        unlock = []
        stack = []

        for i, char in enumerate(s):
            if not int(locked[i]):
                unlock.append(i)
                continue

            if char == '(':
                stack.append(i)
            if char == ')':
                if not stack:
                    if unlock:
                        unlock.pop()
                    else:
                        return False
                else:
                    stack.pop()


        if not stack:
            return True

        p = 0
        for paren in stack:
            
            while p < len(unlock):
                if unlock[p] < paren:
                    p +=1
                else:
                    p +=1
                    break
            else:
                return False        

        return True