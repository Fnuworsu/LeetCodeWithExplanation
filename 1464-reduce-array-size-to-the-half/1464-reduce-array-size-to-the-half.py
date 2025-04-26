class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        """
        total = 10
        3:4
        5:3
        2:2
        7:1
        """
        total = len(arr)
        K = total // 2
        nums = sorted([(-v,k) for k,v in Counter(arr).items()])
        # print(nums, K, total)
        count = 0

        for v,k in nums:
            total += v
            count += 1

            if total <= K:
                return count
        
        return count