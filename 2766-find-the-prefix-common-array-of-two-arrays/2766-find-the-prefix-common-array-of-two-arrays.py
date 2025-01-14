class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        """
        [1,3,2,4]
        [3,1,2,4]
        
        setA = {1,3}
        setB = {3,1}
        """
        setA = set()
        setB = set()
        res = []

        for a,b in zip(A, B):
            setA.add(a)
            setB.add(b)

            res.append(len(setA.intersection(setB)))
        
        return res