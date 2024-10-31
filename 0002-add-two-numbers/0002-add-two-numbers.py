# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, node):
        """
        Reverse any node, based of node.val
        """
        res, curr = [], node

        while curr:
            res.append(str(curr.val))
            curr = curr.next

        return int("".join(reversed(res))) 

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l, r = self.reverse(l1), self.reverse(l2)
        print(l)
        print(r)
        Sum = l + r
        
        res = []

        if Sum == 0:
            res.append(0)

        else:
            while Sum > 0:
                res.append(Sum % 10)
                Sum = Sum // 10
            
        print(res)
        dummy = ListNode()
        curr = dummy

        for n in res:
            node = ListNode(n)
            curr.next = node
            curr = curr.next

        return dummy.next



        