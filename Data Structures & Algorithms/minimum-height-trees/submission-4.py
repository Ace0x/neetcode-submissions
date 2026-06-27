from collections import defaultdict
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if len(edges) == 0:
            return [0]
        dc = defaultdict(set)
        
        for s,e in edges:
            dc[s].add(e)
            dc[e].add(s)
        #print(dc)

        edges = {}
        leaves = []
        
        for src,nei in dc.items():
            if len(nei) == 1:
                leaves.append(src)
            edges[src] = len(nei)
        
        while leaves:
            if n <= 2:
                return leaves
            for i in range(len(leaves)):
                node = leaves.pop(0)
                n -= 1
                for nei in dc[node]:
                    edges[nei] -= 1
                    if edges[nei] == 1:
                        leaves.append(nei)
                    

        """visited = set()
        
        def dfs(i,c,h):
            
            if i in visited:
                return h
            #print(i,c,h)
            visited.add(i)
            h = max(h,c)
            for node in dc[i]:
                h = max(h,dfs(node,c+1,h))
            
            return h
        best = float('inf')
        res = []
        for key in dc:
            visited = set()
            r = dfs(key,0,0)
            if r == best:
                res.append(key)
            if r < best:
                res = [key]
                best = r
            #print(res)
        
        return res"""