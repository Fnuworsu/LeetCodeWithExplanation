class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        """
        n = 1,2,3,4
        [1,3,2,4]
        [3,1,2,4]

        set1 = 1
        set2 = 3
        """
        res = []
        set1, set2 = set(), set()

        for x,y in zip(A, B):
            set1.add(x)
            set2.add(y)

            res.append(len(set1 & set2))
        
        return res