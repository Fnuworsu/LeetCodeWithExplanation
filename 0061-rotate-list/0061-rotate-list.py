# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        brute force
        [1,2,3,4,5]
        [5,4,3,2,1]
        """
        if not head or not k:
            return head
            
        nums = deque()
        
        while head:
            nums.append(head.val)
            head = head.next
        
        k = k % len(nums)

        while k > 0:
            nums.appendleft(nums.pop())
            k -= 1
        
        temp = ListNode()
        curr = temp

        for n in nums:
            curr.next = ListNode(n)
            curr = curr.next
        
        return temp.next

        