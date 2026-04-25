class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        for i in range(len(s)):
            if not d.get(s[i]):
                d[s[i]] = 0
            d[s[i]] += 1
        for i in range(len(t)):
            if not d.get(t[i]):
                return False
            d[t[i]] += 1
        for i in d.values():
            if i % 2 != 0:
                return False
        return True
