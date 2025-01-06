class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        loc = []

        for i in range(len(boxes)):
            if boxes[i] == '1':
                loc.append(i)

        res = []

        for i in range(len(boxes)):
            resTotal = 0
            for j in loc:
                resTotal += abs(i-j)
            res.append(resTotal)

        return res                

        