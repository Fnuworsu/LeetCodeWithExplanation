# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findSuccessor(node):
            node = node.right
            
            while node.left:
                node = node.left
            
            return node
        
        def delete(node, key):
            if not node:
                return node
            
            if key > node.val:
                node.right = delete(node.right, key)
            
            elif key < node.val:
                node.left = delete(node.left, key)
            
            else:
                if not node.left and not node.right:
                    node = None
                elif not node.left:
                    node = node.right
                elif not node.right:
                    node = node.left
                else:
                    successor = findSuccessor(node)
                    node.val = successor.val
                    node.right = delete(node.right, successor.val)
            
            return node
        
        return delete(root, key)
        