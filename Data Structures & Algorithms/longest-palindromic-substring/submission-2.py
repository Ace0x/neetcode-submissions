"""class Solution:
    def longestPalindrome(self, s: str) -> str:
        


        word = {}
        largest = ''
        i = 0
        while i < len(s):
            ls = ''
            rs = ''
            tmp = i
            j = len(s) - 1
            while not i > j:
                print(i,j)
                if i == j:
                    ls += s[i]
                    if len(ls+rs) > len(largest):
                        largest = ls+rs
                    break
                if i > j:
                    break
                left = s[i]
                right = s[j]
               
                if left != right:
                    ls = ''
                    rs = ''
                    i = tmp
                    j -= 1
                    continue
                
                
                ls += s[i]
                rs = s[j] + rs
                print(ls,i,rs,j)
                j -= 1
                
                i += 1

            if i > j and len(ls+rs) > len(largest):
                largest = ls+rs
            
            i = tmp + 1

            
            
        return largest """

class Solution:
    def longestPalindrome(self, s: str) -> str:
        largest = ""

        start = 0
        while start < len(s):
            end = len(s) - 1

            while end >= start:
                l = start
                r = end

                while l <= r:
                    if s[l] != s[r]:
                        break
                    l += 1
                    r -= 1

                # If we crossed, the whole substring was a palindrome
                if l > r:
                    candidate = s[start:end + 1]
                    if len(candidate) > len(largest):
                        largest = candidate
                    break  # no need to try smaller endings for this start

                end -= 1

            start += 1

        return largest