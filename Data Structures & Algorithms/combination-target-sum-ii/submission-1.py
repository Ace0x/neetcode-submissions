class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        candidates = sorted(candidates)
        def combi(ls,s,i):
            if s == target:
                res.append(ls)
                return
            for j in range(i,len(candidates)):
                
                if s > target:
                    break

                if j > i and candidates[j] == candidates[j-1]:
                    continue


                combi(ls + [candidates[j]],s + candidates[j],j+1)    
          
        
        combi([],0,0)
        return res
