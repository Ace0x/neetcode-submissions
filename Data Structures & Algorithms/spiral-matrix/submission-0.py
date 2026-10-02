class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []

        if len(matrix) == 0:
            return res

        n = 0
        # 0 = right
        # 1 = down
        # 2 = left
        # 3 = up

        def dfs(i, j, visited):
            nonlocal n

            visited.add((i, j))
            res.append(matrix[i][j])

            # We've visited everything
            if len(visited) == len(matrix) * len(matrix[0]):
                return res

            if n == 0:
                ni, nj = i, j + 1

            elif n == 1:
                ni, nj = i + 1, j

            elif n == 2:
                ni, nj = i, j - 1

            else:  # n == 3
                ni, nj = i - 1, j

            # If next position is invalid, rotate direction
            if (
                ni < 0
                or nj < 0
                or ni >= len(matrix)
                or nj >= len(matrix[0])
                or (ni, nj) in visited
            ):
                n = (n + 1) % 4

                # Calculate next position again using new direction
                if n == 0:
                    ni, nj = i, j + 1
                elif n == 1:
                    ni, nj = i + 1, j
                elif n == 2:
                    ni, nj = i, j - 1
                else:
                    ni, nj = i - 1, j

            return dfs(ni, nj, visited)
        return dfs(0,0,set())
            

