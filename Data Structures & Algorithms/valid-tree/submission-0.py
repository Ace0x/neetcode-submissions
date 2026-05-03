from collections import defaultdict
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        n nodes from 0 to n-1
        undirected edges
        """

        # A tree with n nodes must have exactly n - 1 edges
        if len(edges) != n - 1:
            return False

        visit = defaultdict(list)

        # Undirected graph: add both directions
        for node in edges:
            visit[node[0]].append(node[1])
            visit[node[1]].append(node[0])

        def dfs(i, parent, visited):
            if i in visited:
                return False, visited

            visited.add(i)

            for node in visit[i]:
                # In an undirected graph, seeing your parent again is normal
                if node == parent:
                    continue

                acy, visited = dfs(node, i, visited)

                # Propagate failure upward
                if not acy:
                    return False, visited

            return True, visited

        acy, reached = dfs(0, -1, set())

        if acy and len(reached) == n:
            return True
        else:
            return False