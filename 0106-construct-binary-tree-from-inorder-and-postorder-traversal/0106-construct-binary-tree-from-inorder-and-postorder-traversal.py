# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        """
        in -> l n r [9,3,15,20,7]
        pos-> l r n [9,15,7,20,3]
        root = 3
        """
        def dfs(arr1, arr2):
            if not arr1 or not arr2:
                return None

            root = TreeNode(arr2[-1])
            idx = arr1.index(arr2[-1])

            root.left = dfs(arr1[:idx], arr2[:idx])  
            root.right = dfs(arr1[idx+1:], arr2[idx:-1])

            return root  

        return dfs(inorder, postorder)    
        