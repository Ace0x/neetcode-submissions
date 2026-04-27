from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])
        INF = 2147483647

        q = deque()

        # Add all treasures as starting points
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 0:
                    q.append((i, j))

        directions = [
            (1, 0),
            (-1, 0),
            (0, 1),
            (0, -1)
        ]

        while q:
            i, j = q.popleft()

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if ni < 0 or ni >= ROWS or nj < 0 or nj >= COLS:
                    continue

                # Only update unvisited empty rooms
                if grid[ni][nj] != INF:
                    continue

                grid[ni][nj] = grid[i][j] + 1
                q.append((ni, nj))