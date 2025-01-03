from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        """
        Counts the number of valid splits such that the sum of the left part
        is greater than or equal to the sum of the right part.
        """
        total = sum(nums)  # Calculate the total sum of the array
        acc = 0  # Running sum of the left part
        res = 0  # Counter for valid splits

        # Iterate over indices where a split is possible
        for i in range(len(nums) - 1):
            acc += nums[i]  # Update the running sum of the left part
            if acc >= total - acc:  # Check if the left part is >= right part
                res += 1

        return res
