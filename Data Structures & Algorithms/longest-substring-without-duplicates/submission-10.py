class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0, 0
        largest = 0
        sup = dict()
        while r < len(s):
            c = sup.get(ord(s[r]))
            if not c == None:
                if not c < l:
                    l = sup[ord(s[r])] + 1
            sup[ord(s[r])] = r
            largest = max(r - l + 1,largest)
            r += 1
        
        return largest
