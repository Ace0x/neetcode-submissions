class LRUCache:

    def __init__(self, capacity: int):
        self.cache = []
        self.capacity = capacity
        #print(capacity)

    def get(self, key: int) -> int:
        #print(self.cache)
        for i in range(len(self.cache)):
            if self.cache[-i]:
                if self.cache[-i][0] == key:
                    x = self.cache.pop(-i)
                    #print("pop",x)
                    self.cache.append(x)
                    print("get ",x," cache ",self.cache)
                    return self.cache[-1][1]
        return -1


    def put(self, key: int, value: int) -> None:
        for i in range(len(self.cache)):
            if self.cache[-i]:
                if self.cache[-i][0] == key:
                    self.cache.pop(-i)
                    self.cache.append((key,value))
                    #print("put update" ,x," cache ",self.cache)
                    return None
            
        if len(self.cache) < self.capacity:
            #print("put appended ",(key,value)," cache ",self.cache)
            self.cache.append((key,value))
        else:
            #print("put popped",(key,value)," cache ",self.cache)
            self.cache.pop(0)
            self.cache.append((key,value))
        

