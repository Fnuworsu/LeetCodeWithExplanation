# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        nlr
        Do not return anything, modify root in-place instead.
        """
        if not root or (not root.left and not root.right):
            return

        def dfs(node):
            if not node:
                return []
            
            return [node] + dfs(node.left) + dfs(node.right)
        
        curr = root
        preOrder = dfs(root)

        for i in range(1, len(preOrder)-1):
            node = preOrder[i]
            nxt = preOrder[i+1]

            curr.right = TreeNode(node.val, None, nxt)
            curr.left = None
            curr = curr.right
        
        curr.right = preOrder[-1]
        curr.left = None

        