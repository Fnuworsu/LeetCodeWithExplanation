# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        """
        nums = [-10,-3,0,5,9]
        mid = root
        nums[:mid] = root.left
        nums[mid+1] = root.left
        """
        def makeTree(arr, l, r):
            if l > r:
                return

            m = (l+r) // 2

            root = TreeNode(arr[m])
            root.left = makeTree(arr, l, m-1)
            root.right = makeTree(arr, m+1, r)

            return root

        root = makeTree(nums, 0, len(nums)-1)

        return root        
            
        