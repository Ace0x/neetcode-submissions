class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        d = dict()
        c = dict()

        for i in range(len(s)):

            d[s[i]] = 1 + d.get(s[i], 0)
            c[t[i]] = 1 + c.get(t[i], 0)
        for i in c:
            if c[i] != d.get(i,0):
                return False
        return True