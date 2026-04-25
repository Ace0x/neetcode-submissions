class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        val = dict()
        for i in s1:
            val[i] = val.get(i, 0) + 1
        
        l = 0
        r = 0
        required = len(s1)  # Total characters we need to match
        
        while r < len(s2):
            # 1. ADD NEW CHAR (at r)
            # If the new char is one we want (it's in our map)
            if s2[r] in val:
                # If the count is > 0, it means this is a "useful" match
                if val[s2[r]] > 0:
                    required -= 1
                # Decrement the count in the map
                val[s2[r]] -= 1
            
            # 2. SHRINK WINDOW (at l)
            # If window is larger than len(s1), we must slide l forward
            if (r - l + 1) > len(s1):
                # If the char leaving was one we were tracking
                if s2[l] in val:
                    # If the count is >= 0, it means we are losing a "useful" char
                    # (We use >= 0 because we decremented it earlier)
                    if val[s2[l]] >= 0:
                        required += 1
                    val[s2[l]] += 1
                l += 1
            
            # 3. CHECK SUCCESS
            # If we found all required chars and window size is exactly len(s1)
            if required == 0:
                return True
                
            r += 1
            
        return False
                    
                    

