# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def back(node, target, path):
            nonlocal res

            if not node:
                return
            
            if not node.left and not node.right:
                if node.val == target:
                    path.append(node.val)
                    res.append(path[:])
                    path.pop()
                return
            
            path.append(node.val)

            l = back(node.left, target-node.val, path)
            r = back(node.right, target-node.val, path)

            path.pop()
        
        back(root, targetSum, [])

        return res