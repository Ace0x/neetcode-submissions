class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses = 0
        dependency = set()
        taking = set()
        uniq = set()
        
        for i in prerequisites:
            if i[1] == i[0]:
                return False
           
            if i[1] not in dependency:
                dependency.add(i[1])
            if i[0] not in taking:
                taking.add(i[0])
            if dependency.issubset(taking) or taking.issubset(dependency) and len(dependency) != 0:
                return False
            
            uniq.add(i[0])
            uniq.add(i[1])
            
        #print(dependency, taking)
        
        if len(uniq) <= numCourses:
            return True
                
        return False