class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()
        total = 0

        for ops in operations:
            if ops == "+":
                x = stack[-1] + stack[-2]
                total += x
                stack.append(x)
            elif ops == "D":
                x = stack[-1] * 2
                total += x
                stack.append(stack[-1] * 2)
            elif ops == "C":
                total -= stack.pop()
            else:
                stack.append(int(ops))
                total += int(ops)
          
        return total
