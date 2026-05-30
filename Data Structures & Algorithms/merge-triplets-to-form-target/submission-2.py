class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        
        good = [0, 0, 0]

        for t in triplets:
            # poison triplet: would overshoot target
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue

            good[0] = max(good[0], t[0])
            good[1] = max(good[1], t[1])
            good[2] = max(good[2], t[2])

        return good == target
    

