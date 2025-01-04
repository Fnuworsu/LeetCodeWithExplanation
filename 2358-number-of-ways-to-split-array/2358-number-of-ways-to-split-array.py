class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        """
        split idx:
            1.sum of(i+1) el >= sum(n-i-1)
            2. one or more elements to the right of i

        [10,4,-8,7]  
        total = 13
        0 <= i < n-1
        [10,14,6,13]
        res = 1o  
        10 -> 10, 10
        """
        prefix = [nums[0]]

        for n in nums[1:]:
            prefix.append(prefix[-1] + n)
        # print(prefix)    

        res, acc = 0, 0

        for i in range(len(nums)-1):    
            acc += nums[i]
            p = prefix[i]
            s = prefix[-1] - acc

            if p >= s:
                res += 1

        return res        

        