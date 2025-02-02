class Solution:
    def check(self, nums: List[int]) -> bool:
        arr = deque(sorted(nums))
        nums = deque(nums)

        k = len(nums)

        while k:
            addOn = nums.popleft()
            nums.append(addOn)
            # print(nums)
            if nums == arr:
                return True
            
            k -= 1
        
        return False
