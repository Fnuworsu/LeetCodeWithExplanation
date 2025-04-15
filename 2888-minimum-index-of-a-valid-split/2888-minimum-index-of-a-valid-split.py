class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        """
        x => d if > n/2 == x (only one in arr)
        counter = {1:5, 2:1, 3:1, 7:1}

        freq = {2:1}
        x = 1

         0 1 2 3 4 5 6 7 8 9
        [2,1,3,1,1,1,7,1,2,1]
        """
        N = len(nums)
        count = Counter(nums)
        major = -1
        gain = 0

        for k,v in count.items():
            if v > N//2:
                major = [k,v]
                break
        
        for i,n in enumerate(nums):
            if n == major[0]:
                major[1] -= 1
                gain += 1
            
            x = i+1
            y = N - x

            # print(len(nums[i+1:]), N-x, x, len(nums[:i+1]))
            
            if gain > x // 2 and major[1] > y // 2:
                return i
        
        return -1
