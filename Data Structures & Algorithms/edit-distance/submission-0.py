class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        memo = {}

        def dfs(i, j):
            # If word1 is exhausted, insert the rest of word2
            if i == len(word1):
                return len(word2) - j

            # If word2 is exhausted, delete the rest of word1
            if j == len(word2):
                return len(word1) - i

            if (i, j) in memo:
                return memo[(i, j)]

            # Characters already match, no edit needed
            if word1[i] == word2[j]:
                memo[(i, j)] = dfs(i + 1, j + 1)
            else:
                delete = dfs(i + 1, j)
                insert = dfs(i, j + 1)
                replace = dfs(i + 1, j + 1)

                memo[(i, j)] = 1 + min(delete, insert, replace)

            return memo[(i, j)]

        return dfs(0, 0)


            

      


            
            
            