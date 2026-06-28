class Solution:
    def myPow(self, x: float, n: int) -> float:
   

        def help(x,n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            res = help(x,n//2)
            res *= res
            #print(n%2)
            return x * res if n % 2 else res
            

        res = help(x,abs(n))
        return res if n >= 0 else 1/res