class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """
        + -
        n1 = n2: pop n1 and n2
        if n1 < n2: consistently pop 
        """
        stack = []

        for a in asteroids:
            while a != "#" and stack and stack[-1] > 0 and a < 0:
                diff = a + stack[-1]
                if diff < 0:
                    stack.pop()
                elif diff > 0:
                    a = "#"
                else:
                    a = "#"
                    stack.pop()
                    
            if a != "#":
                stack.append(a)
        
        return stack
