class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        skipped = nums.copy()
        def perm(ls,sk):
            if len(sk) == 1:
                res.append((ls + sk).copy())
                return
            
            for _ in range(len(sk)):
                # CHOOSE: Take the first element from the available pool
                val = sk.pop(0)
                ls.append(val)

                # EXPLORE: Recurse with the new state
                perm(ls, sk)

                # BACKTRACK: Remove from our current permutation and put back in pool
                ls.pop()
                sk.append(val)
        perm([],skipped)
        return res

            

