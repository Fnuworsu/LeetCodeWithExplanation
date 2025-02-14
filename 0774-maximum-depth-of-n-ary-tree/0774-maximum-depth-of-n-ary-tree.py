"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0

        level = 0
        q = deque([root])

        while q:
            currL = len(q)

            for _ in range(currL):
                node = q.popleft()
                if not node:
                    continue
                
                for child in node.children:
                    q.append(child)
            level += 1
        
        return level
        