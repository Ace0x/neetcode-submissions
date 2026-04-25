class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        if len(board) == 0:
            return False
        RES = None
        
        def grids(row,col,let,count,visited):
            nonlocal RES
            
            if visited.get((row,col)):
                return
            visited[(row,col)] = True
            if board[row][col] != let:
                return
            count+=1
            
            if count == len(word):
                RES = True
                return True
            if row >= 1:
                grids(row-1,col,word[count],count,visited.copy())
            if row < len(board)-1:
                grids(row+1,col,word[count],count,visited.copy())
            if col >= 1:
                grids(row,col-1,word[count],count,visited.copy())
            if col < len(board[0])-1:
                grids(row,col+1,word[count],count,visited.copy())

        for i in range(len(board)):
            for j in range(len(board[0])):
                curr = board[i][j]
                if curr == word[0]:
                    grids(i,j,curr,0, dict())
                    
                if RES:
                    return True
    
        return False

"""
    def exist(self, board, word):
        if not board:
            return False

        ROWS, COLS = len(board), len(board[0])

        def dfs(row, col, count):
            # If we've matched all letters, we found the word
            if count == len(word):
                return True

            # Out of bounds, or the letter doesn't match
            if (row < 0 or row >= ROWS or 
                col < 0 or col >= COLS or 
                board[row][col] != word[count]):
                return False

            # Mark the current cell as visited by temporarily changing its value
            temp = board[row][col]
            board[row][col] = '#'

            # Explore all 4 adjacent directions (the 'or' automatically bubbles up True)
            found = (dfs(row + 1, col, count + 1) or
                     dfs(row - 1, col, count + 1) or
                     dfs(row, col + 1, count + 1) or
                     dfs(row, col - 1, count + 1))

            # BACKTRACK: Revert the cell back to its original letter for other paths to use
            board[row][col] = temp
            
            return found

        for i in range(ROWS):
            for j in range(COLS):
                # Start DFS if the first letter matches
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True

        return False