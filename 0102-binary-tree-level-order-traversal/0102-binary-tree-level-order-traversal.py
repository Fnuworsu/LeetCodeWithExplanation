# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def bfs(node):
            q = deque([node])
            
            while q:
                level = []
                for _ in range(len(q)):
                    curr = q.popleft()
                    if curr:
                        level.append(curr.val)
                        q.append(curr.left)
                        q.append(curr.right)

                if level:
                    res.append(level)
        bfs(root)
        
        return res                    


        