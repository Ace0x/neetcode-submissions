from collections import defaultdict
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        steps = 0
        s = 0
        q = []

        dc = defaultdict(list)

        for i in flights:
            dc[i[0]].append((i[1], i[2]))

        memo = {}

        def dfs(node, cost, steps):
            if steps > k + 1:
                return float("inf")

            if node == dst:
                return cost

            key = (node, steps)

            if key in memo:
                return cost + memo[key]

            best = float("inf")

            for nei, price in dc[node]:
                candidate = dfs(nei, cost + price, steps + 1)
                best = min(best, candidate)

            memo[key] = best - cost
            return best

        best = dfs(src, 0, 0)
        return best if best != float("inf") else -1