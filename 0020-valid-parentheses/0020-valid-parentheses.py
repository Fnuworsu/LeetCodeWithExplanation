class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {")":"(", "}":"{", "]":"["}
        stack = []

        for c in s:
            #if we meet a close brackect
            if c in closeToOpen:
                if stack and closeToOpen[c] == stack[-1]:
                    stack.pop()
                #if they do not match
                else:
                    return False
            else:
                stack.append(c)

        return not stack                   
        