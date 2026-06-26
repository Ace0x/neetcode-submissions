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
        visited = set()
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
        
        return res