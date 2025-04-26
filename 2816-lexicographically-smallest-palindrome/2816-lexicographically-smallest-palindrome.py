class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        """
                r
        s e v e n
        l
        """
        arr = [c for c in s]
        l, r = 0, len(arr)-1
        val = lambda c: ord(c) - ord('a') + 1

        while l < r:
            if arr[l] != arr[r]:
                if val(arr[l]) < val(arr[r]):
                    arr[r] = arr[l]
                else:
                    arr[l] = arr[r]
            
            l += 1
            r -= 1
        
        return ''.join(arr)