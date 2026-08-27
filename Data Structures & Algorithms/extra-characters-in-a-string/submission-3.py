from functools import cache
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        juan = 0
        dos = 0
        @cache
        def dfs(x):
            if x >= len(s):
                return 0

            attempts = [1 + dfs(x + 1)]

            for key in dictionary:
                l = len(key)

                if s[x:x+l] == key:
                    attempts.append(dfs(x + l))

            return min(attempts)

        return dfs(0)