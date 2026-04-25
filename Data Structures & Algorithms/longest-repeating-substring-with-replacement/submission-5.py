class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        counts = defaultdict(int)
        l, r = 0,0
        maxf = 0
        best = 0

        for r in range(len(s)):
            ch =  s[r]
            counts[ch] += 1
            maxf = max(maxf,counts[ch])
            while r - l + 1 - maxf > k:
                counts[s[l]] -= 1
                l += 1
            best = max(r-l+1,best)
        return best
