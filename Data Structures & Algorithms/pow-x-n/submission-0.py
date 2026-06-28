class Solution:
    def myPow(self, x: float, n: int) -> float:
        original = x
        res = 1
        for i in range(abs(n)):
            if n < 0:
                res *= (1/original)
                #print(res)
            else:
                res *= original 
        return res