class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        ans = []


        def dfs(x, current):
            if len(current) == k:
                ans.append(current.copy())
                return

            if x > n:
                return

            # Take x
            current.append(x)
            dfs(x + 1, current)

            # Undo taking x
            current.pop()

            # Don't take x
            dfs(x + 1, current)

        dfs(1, [])

        return ans
                
                
                    
                

                