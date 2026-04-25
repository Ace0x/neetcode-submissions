class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        grids = defaultdict(set) #tuple position
        for i in range(len(board)):
            for j in range(len(board)):
                val = board[i][j]
                if val == ".":
                    continue
                if cols.get(j) and val in cols.get(j):
                    return False
                if rows.get(i) and val in rows.get(i):
                    return False
                if grids.get((i//3,j//3)) and val in grids.get((i//3,j//3)):
                    return False
                cols[j].add(val)
                rows[i].add(val)
                grids[(i//3,j//3)].add(val)
        return True                