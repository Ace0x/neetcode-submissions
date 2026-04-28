
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        ROWS, COLS = len(grid), len(grid[0])
        rotten = set()
        q = deque()
        cnt = 0
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    rotten.add((i,j))
                    q.append((i,j))
                    cnt += 1
                if grid[i][j] == 1:
                    cnt += 1
        if cnt == 0:
            return 0
        def bfs(i,j):
            if i < 0 or i == ROWS or j < 0 or j == COLS or grid[i][j] == 2 or grid[i][j] == 0:
                return
            grid[i][j] = 2
            q.append((i,j))
            rotten.add((i,j))
        bananas = 0
        time = 0
        while q:

            for i in range(len(q)):
                #print(q)
                r1,r2 = q.popleft()
                bfs(r1+1,r2)
                bfs(r1-1,r2)
                bfs(r1,r2+1)
                bfs(r1,r2-1)
                bananas += 1
            time += 1
            
        
        #bananas += 1
        #print(bananas)
        #print(cnt)
        #print(len(rotten))
        
        #print(time)
        return time-1 if len(rotten) == cnt else -1
                

 
        