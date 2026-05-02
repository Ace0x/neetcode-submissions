class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        depend = [0] * numCourses
        
        unlock = [[] for _ in range(numCourses)]

        for req in prerequisites:
            depend[req[0]] += 1
            unlock[req[1]].append(req[0])
        
        #print(depend)
        
        #print(unlock)
        
        q = deque()
        for i in range(len(depend)):
            if depend[i] == 0:
                q.append(i)
        #print(q)
        taken = []
        while q:
            course = q.popleft()
            taken.append(course)
            #print(course , " " , unlock[course],"iter")
            for c in unlock[course]:
                #print(course , " " , unlock[course],"iter")
                #print(depend," ",c)
                depend[c] -= 1    
                #print(depend," ",c)
                if depend[c] <= 0:
                    #print("trigger")
                    q.append(c)
        #print(taken)
        return taken if len(taken) == numCourses else []