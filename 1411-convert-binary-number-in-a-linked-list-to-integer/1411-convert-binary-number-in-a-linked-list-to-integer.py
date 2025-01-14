# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        """
        101
        1 * 2**0 = 1
        0 * 2**1 = 0
        1 * 2**2 = 4
        """
        def rev(node):
            prev = None

            while node:
                nxt = node.next
                node.next = prev
                prev = node
                #move pointer
                node = nxt
            
            return prev
        
        node = rev(head)
        
        def solve(root, res, exp):
            if not root:
                return res
            
            add = 2**exp
            res += (root.val * add)
            root = root.next

            ans = solve(root, res, exp+1)
            return ans

        return(solve(node, 0, 0))
        
        