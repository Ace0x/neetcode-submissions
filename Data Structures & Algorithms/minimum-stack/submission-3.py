class MinStack:

    def __init__(self):
        self.arr = []
        self.m = float('inf')
    def push(self, val: int) -> None:
        if val < self.m:
            self.m = val
        self.arr.append((val,self.m))
        #print('push: ',self.arr)


    def pop(self) -> None:
        self.arr = self.arr[:len(self.arr)-1]
        if len(self.arr) > 0:
            self.m = self.arr[-1][1]
        else:
            self.m = float('inf')
        #print('pop: ',self.arr)

    def top(self) -> int:
        #print('top: ',self.arr)
        return self.arr[-1][0]        

    def getMin(self) -> int:
        #print('min: ',self.arr)
        return self.arr[-1][1]
