class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        nstr = str(n)
        plus = 0
        mult = 1
        for i in range(len(nstr)):
            plus = plus + int(nstr[i])
            mult = mult * int(nstr[i])
        x = abs(plus - mult)
        return x
Solution().subtractProductAndSum(234)