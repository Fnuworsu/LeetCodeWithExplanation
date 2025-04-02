class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        """
        if s * p >= k and p is the lowest portion at index i, then len(portions) - i will be a
        good pair 
        """
        potions.sort()
        n = len(potions)

        def bs(l,r,s):
            res = float("inf")

            while l <= r:
                mid = (l + r) // 2

                if (s * potions[mid]) >= success:
                    res = min(res, mid)
                    r = mid - 1
                else:
                    l = mid + 1
            
            return res if res != float("inf") else n
        
        ans = []

        for s in spells:
            add = bs(0, n-1, s)
            ans.append(n-add)
        
        return ans
    
    """
    space complexity: O(n)
    time complexity: O(nlogn) + O(nlog(n)) => O(nlogn)
    """
