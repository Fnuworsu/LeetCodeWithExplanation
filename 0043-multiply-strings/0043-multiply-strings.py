class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if "0" in [num1, num2]:
            return "0"
        
        """
        2 1 0

        4 5 6
        1 2 3
        _____
      1 3 6 8 
        """
        num1, num2 = num1[::-1], num2[::-1]
        res = [0 for _ in range(len(num1) + len(num2))]

        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += res[i1 + i2] // 10
                res[i1 + i2] = res[i1 + i2] % 10

        res, beg = res[::-1], 0

        while beg < len(res) and res[beg] == 0:
            beg += 1

        res = map(str, res[beg:])

        return "".join(res) 