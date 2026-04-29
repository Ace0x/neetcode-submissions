class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(i, j, visited, prev_height):
            if (
                (i, j) in visited
                or i < 0 or j < 0
                or i == ROWS or j == COLS
                or heights[i][j] < prev_height   # can't flow down to us, so we can't go up to it
            ):
                return
            visited.add((i, j))
            h = heights[i][j]
            dfs(i + 1, j, visited, h)
            dfs(i - 1, j, visited, h)
            dfs(i, j + 1, visited, h)
            dfs(i, j - 1, visited, h)

        # Pacific = top + left; Atlantic = bottom + right
        for c in range(COLS):
            dfs(0, c, pac, heights[0][c])
            dfs(ROWS - 1, c, atl, heights[ROWS - 1][c])
        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS - 1, atl, heights[r][COLS - 1])

        return [[r, c] for r in range(ROWS) for c in range(COLS) if (r, c) in pac and (r, c) in atl]

"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        ROWS = len(heights)
        COLS = len(heights[0])

     

        def hydro_check(i,j,pacific,atlantic):
            if i == 0 or j == 0:
                pacific = True
            if i == ROWS-1 or j == COLS - 1:
                atlantic = True
            #print(i," ",j,ROWS-1, COLS-1)
            return pacific, atlantic

        def dfs(prev_i,prev_j,i,j,pacific,atlantic,visited):
            
            if pacific and atlantic:
                return True

            if i < 0 or j < 0 or i == ROWS or j == COLS:
                return

            pacific, atlantic = hydro_check(i,j,pacific,atlantic)
            
            if (i,j) in visited:
                return

            if heights[prev_i][prev_j] < heights[i][j]:
                #print("too big")
                return
            
            visited.add((i,j))
            
            #print(i,j," ", heights[prev_i][prev_j] ," ", heights[i][j], " ",pacific,atlantic)

            if pacific and atlantic:
                return True
            return (
                dfs(i,j,i+1,j,pacific,atlantic,visited.copy()) or
                dfs(i,j,i-1,j,pacific,atlantic,visited.copy()) or
                dfs(i,j,i,j+1,pacific,atlantic,visited.copy()) or
                dfs(i,j,i,j-1,pacific,atlantic,visited.copy())
            )
           
        
        res = []
        for i in range(ROWS):
            for j in range(COLS):
                #print("yay")
                
                if dfs(i,j,i,j,False,False,set()):
                    res.append([i,j])
        #print(res)
        return res
                    
                


"""