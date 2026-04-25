class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")

        j = len(s) -1
        for i in range(len(s)):
            if i == j:
                break
            if not s[j].isalnum():
                j -=1
            if not s[i].isalnum():
                continue
            if s[i].lower() != s[j].lower():
                return False
            j-=1
            
        return True