from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        mp = defaultdict(list)
   
        for edge in edges:
            mp[edge[0]].append(edge[1])
            mp[edge[1]].append(edge[0])
            
      

        ctr = 0
        visited = set()

        def dfs(node):
            
            if node in visited:
                return
            #print(node," ")
            visited.add(node)
    
            #print("here", mp[node])

            for nod in mp[node]:
                #print(nod)

                dfs(nod)
            return
        #print(mp)
        #dfs(list(nodes)[0])
        #print(visited)
        #print(nodes)
        #print(mp.keys())
       
        for node in range(n):
           
            if node in visited:
                continue
            
            #print(node)
            #print(node)
            dfs(node)
            ctr += 1
        #print(visited, ctr)
        for i in range(n):
            if i not in visited:
                ctr += 1
        return ctr

        