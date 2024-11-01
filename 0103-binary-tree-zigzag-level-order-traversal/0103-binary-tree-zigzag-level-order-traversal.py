# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        def bfs(root):
            q = deque([root])
            qLen = len(q)
            zig = 1

            while q:
                level = []
                for _ in range(len(q)):
                    node = q.popleft()
                    if node:
                        level.append(node.val)
                        q.append(node.left)
                        q.append(node.right)

                if level and zig > 0:
                    res.append(level)        
                elif level and zig < 0:
                    res.append(level[::-1])
                zig *= -1    

        bfs(root)

        return res                

        