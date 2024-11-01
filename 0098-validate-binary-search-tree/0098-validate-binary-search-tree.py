# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, maxL=float("-inf"), minR=float("inf")):
            if not node:
                return True

            if node.val > maxL  and node.val < minR:
                return valid(node.left, maxL, node.val) and valid(node.right, node.val, minR)

            return False

        return valid(root)       