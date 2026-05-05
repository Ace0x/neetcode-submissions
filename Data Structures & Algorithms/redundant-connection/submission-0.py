from collections import defaultdict, deque

class Solution:
    def findRedundantConnection(self, edges):
        mp = defaultdict(list)

        def has_path(src, target):
            q = deque([src])
            visited = set([src])

            while q:
                node = q.popleft()

                if node == target:
                    return True

                for nei in mp[node]:
                    if nei not in visited:
                        visited.add(nei)
                        q.append(nei)

            return False

        for u, v in edges:
            if u in mp and v in mp and has_path(u, v):
                return [u, v]

            mp[u].append(v)
            mp[v].append(u)