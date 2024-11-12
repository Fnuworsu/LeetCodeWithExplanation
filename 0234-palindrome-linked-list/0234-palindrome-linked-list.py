# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(node):
            prev, curr = None, node

            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            return prev

        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        rev = reverse(slow)
        # print(rev)

        while rev:
            if rev.val != head.val:
                return False
            rev = rev.next
            head = head.next

        return True                
        