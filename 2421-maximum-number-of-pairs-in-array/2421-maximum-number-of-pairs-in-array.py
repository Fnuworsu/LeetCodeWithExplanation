class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        """
        {
            1:2
            3:2
            2:3
        }
        pairs = v//2
        remove = pairs * 2
        rem = 
        """
        hmap = defaultdict(int)
        n = len(nums)
        pairs = 0

        for num in nums:
            hmap[num] += 1

        for v in hmap.values():
            if v > 1:
                p = v // 2
                rem = p * 2

                pairs += p
                n -= rem

        return [pairs, n]  
        