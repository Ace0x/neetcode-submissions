class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def paren(ls,op,close):
            if op == 0 and close == 0:
                res.append(ls)
                return

            if op > 0:
                paren(ls+"(",op-1,close+1)


            if close > 0:
                paren(ls+")",op,close-1)
        paren("",n,0)
        return res
