from collections import defaultdict
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        n = len(s)

        d = defaultdict(list)

        for i in range(n):
            d[s[i]].append(i)

        l = 0
        last = 0
        res = []
        for c in range(n):
            cur = d[s[c]][-1]
            if cur > last:
                last = cur
            if c == last:
                res.append(c + 1 - l)
                l = c + 1
        #print(res)
        return res