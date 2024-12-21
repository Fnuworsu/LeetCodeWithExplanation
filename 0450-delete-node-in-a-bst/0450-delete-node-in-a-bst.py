# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findSuccessor(node):
            # Find the smallest node in the right subtree
            node = node.right
            while node.left:
                node = node.left
            return node

        def delete(node, key):
            if not node:
                return None

            if key > node.val:
                node.right = delete(node.right, key)
            elif key < node.val:
                node.left = delete(node.left, key)
            else:
                # Node to delete found
                if not node.left and not node.right:  # Leaf node
                    return None
                elif not node.left:  # Only right child exists
                    return node.right
                elif not node.right:  # Only left child exists
                    return node.left
                else:
                    # Both children exist
                    successor = findSuccessor(node)
                    node.val = successor.val
                    # Delete the successor from the right subtree
                    node.right = delete(node.right, successor.val)

            return node

        return delete(root, key)
