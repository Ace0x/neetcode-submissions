class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def dfs(i,j):
            if i < len(grid) and i >= 0 and j < len(grid[0]) and j >= 0:
                curr = grid[i][j]
            else:
                return 
            if curr != "1":
                return 
            #print(i,j,"",curr)
            grid[i][j] = 0

            dfs(i+1,j)
            dfs(i,j+1)
            dfs(i-1,j)
            dfs(i,j-1)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i,j)
                    #print("cut")
                    count += 1

        return count