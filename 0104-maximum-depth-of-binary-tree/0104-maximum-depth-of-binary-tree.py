# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(node, h):
            if not node:
                return 0

            stack = [(0,node)]

            while stack:
                l, curr = stack.pop()
                h = max(h, l)

                if curr.left:
                    stack.append((l+1, curr.left))
                if curr.right:
                    stack.append((l+1, curr.right))

            return h+1
        return dfs(root, 0)           
                    

        