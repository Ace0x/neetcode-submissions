class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = [0] * 10
        check = defaultdict(int)
        res = [0] * k
        for i in nums:
            check[i] += 1
            a = check[i]
            for j in range(len(res)):
                if check[res[j]] < a and i not in res:
                    res[j] = i
            
        return res
        