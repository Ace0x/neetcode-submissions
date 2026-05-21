from collections import defaultdict
import heapq
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        # Build adjacency list
        for u, v, w in times:
            graph[u].append((v, w))

        distances = [float("inf")] * (n + 1)
        distances[k] = 0

        heap = [(0, k)]  # (current_distance, node)
        visited = set()

        while heap:
            current_dist, u = heapq.heappop(heap)

            if u in visited:
                continue

            visited.add(u)

            for v, weight in graph[u]:
                if v not in visited:
                    new_dist = current_dist + weight

                    if new_dist < distances[v]:
                        distances[v] = new_dist
                        heapq.heappush(heap, (new_dist, v))
        #print(distances)
        answer = max(distances[1:])

        return answer if answer != float("inf") else -1