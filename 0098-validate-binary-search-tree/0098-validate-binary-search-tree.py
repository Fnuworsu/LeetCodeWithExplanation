# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        global min, max for the root, so that the invariance applies across
        """

        def validate(node, minVal, maxVal):
            if not node:
                return True

            if node.val <= minVal:
                return False

            if node.val >= maxVal:
                return False

            left = validate(node.left, minVal, node.val)
            right = validate(node.right, node.val, maxVal)

            return left and right

        return validate(root, float("-inf"), float("inf"))                