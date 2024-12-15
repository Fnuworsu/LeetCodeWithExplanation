class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        """
        total = (2 x sum) + outlier
        outlier = total -2Sum

        """
        freq = defaultdict(int)
        for n in nums:
            freq[n] += 1

        total = sum(nums)
        maxOut = float("-inf")

        for k in freq.keys():
            out = total - (2*k)

            if out in freq and (out != k or freq[k] > 1):
                maxOut = max(maxOut, out)

        return maxOut          
        