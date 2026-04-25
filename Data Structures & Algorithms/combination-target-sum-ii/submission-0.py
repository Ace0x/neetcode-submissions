class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        # 1. Sort the array so duplicates are adjacent and we can break early
        candidates.sort()
        
        def comb(st, s, i):
            # Base Case: We found a valid combination
            if s == target:
                res.append(st)
                return
            
            # The Engine: Loop through remaining candidates
            for j in range(i, len(candidates)):
                # Optimization: If the current sum + next number is too big, 
                # because the array is sorted, all subsequent numbers will also be too big.
                if s + candidates[j] > target:
                    break
                
                # Magic Line: Skip duplicates at the same tree depth
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                
                # The Recursive Call: We include candidates[j] and move to the next index
                comb(st + [candidates[j]], s + candidates[j], j + 1)
        
        # Kick off the recursion with an empty path, 0 sum, starting at index 0
        comb([], 0, 0)
        
        return res