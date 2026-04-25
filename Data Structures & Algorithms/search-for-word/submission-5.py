class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if len(board) == 0:
            return False
        RES = None
        #print(len(word))
        def grids(row,col,let,count,visited):
            nonlocal RES
            #print(row, ' ', col)
            #print(count,' ',board[row][col], ' ', len(word), ' ', row, ' ', col, ' ', visited)
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
                    #print(RES)
                if RES:
                    return True
        #print(board)
        return False

