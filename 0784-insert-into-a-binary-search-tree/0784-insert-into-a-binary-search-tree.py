# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node, val):
            if not node:
                node = TreeNode(val)
            
            elif node.val > val:
                node.left = dfs(node.left, val)
            else:
                node.right = dfs(node.right, val)
            
            return node

        node = dfs(root, val)
        
        return node
