class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j,total):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
                print(total)
                return total
            
            if grid[i][j] != 1:
                print(total)
                return total
            total +=  1
            
            grid[i][j] = 0

            #print(i,j,"",total)

            total = max(dfs(i+1,j,total),total)
            total = max(dfs(i-1,j,total),total)
            total = max(dfs(i,j+1,total),total)
            total = max(dfs(i,j-1,total),total)

            return total
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                output = dfs(i,j,0)
                #print("output",output)
                res = max(output,res)
        return res

        
