class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        buck = []
        for i in range(len(nums)):
            buck.append([])
        dic = defaultdict(int)
        for i in range(len(nums)):
            dic[nums[i]] += 1
        for c, v in dic.items():
            buck[v-1].append(c)
        res = []
        for i in range(len(buck),0,-1):
            for j in range(len(buck[i-1]),0,-1):
              
                res.append(buck[i-1][j-1])
                if len(res) == k:
                    return res
        return res