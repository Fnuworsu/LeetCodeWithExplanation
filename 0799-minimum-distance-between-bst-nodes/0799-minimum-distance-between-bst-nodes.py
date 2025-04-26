# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return []
            return dfs(node.left) + [node.val] + dfs(node.right)
        
        inorder = dfs(root)
        res = math.inf

        for i in range(len(inorder)-1):
            res = min(res, inorder[i+1] - inorder[i])
        
        return res