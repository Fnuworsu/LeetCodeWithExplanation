"""
q = deque([])
[2,3,4]

[3,4,2]
[4,2,3]
"""
class MyStack:

    def __init__(self):
        self.q = deque([])

    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        print(self.q)    
        return self.q.popleft()   

    def top(self) -> int:   
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())
        res = self.q[0]
        self.q.append(self.q.popleft())
        return res     

    def empty(self) -> bool:
        return not self.q
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()