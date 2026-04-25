class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        i = 0
        r = len(matrix[0]) - 1
        l = 0
        while l <= r and i < len(matrix):
            mid = l + (r - l) // 2
            print(i)
            print(mid)
            
            if target > matrix[i][r]:
                i += 1
                continue
            if target == matrix[i][mid]:
                return True
            if target < matrix[i][mid]:
                r = mid - 1
            else:
                l = mid + 1
        return False
