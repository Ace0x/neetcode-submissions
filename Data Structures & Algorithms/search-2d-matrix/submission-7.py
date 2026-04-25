class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = len(matrix) // 2
        r = len(matrix[0]) - 1
        l = 0
        f, y = 0, 0
        while l <= r and i < len(matrix) and i >= 0:
            mid = l + (r - l) // 2
            if target == matrix[i][mid]:
                return True
            if target > matrix[i][r] and not f:
                i += 1
                y = 1
                continue
            elif target < matrix[i][l] and not y:
                i -=1
                f = 1
                continue 
            if target < matrix[i][mid]:
                r = mid - 1
            else:
                l = mid + 1
        return False
