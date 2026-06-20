class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        n = len(asteroids)
        if n <= 1:
            return asteroids
        
        l = 0
        r = 1
        mark = set()
        while r < n:
            cl = asteroids[l]
            cr = asteroids[r]
            
            if (cr < 0 and cl > 0):
                if abs(cl) == abs(cr):
                    mark.add(l)
                    mark.add(r)
                    r += 1
                    while l in mark:
                        l -= 1
                        #print(l,r,mark)
                    if l < 0:
                        l = r
                        r += 1
                elif abs(cl) < abs(cr):
                    mark.add(l)
                    while l in mark:
                        l -= 1
                    if l < 0:
                        l = r
                        r += 1
                elif abs(cl) > abs(cr):
                    mark.add(r)
                    r += 1
                #print(mark,l,r)
            else:
                l = r
                r += 1
            
        #print(mark)
        return [asteroids[i]for i in range(n) if i not in mark]