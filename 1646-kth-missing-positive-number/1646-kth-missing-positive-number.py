class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        s1 = SortedSet(arr)
        s2 = SortedSet([x for x in range(1, arr[-1] + k + 1)])

        res = list(s1 ^ s2)
        return res[(k % len(res))-1]