class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        y = set(('(','[','{'))
        for i in s:
            a.append(i)
            if i not in y and len(a) != 0:
                c = a.pop()
                if len(a) == 0:
                    return False
                b = a.pop()
                #print("b ",b,"c ",c)
                if c == ")" and b != "(":
                    return False
                if c == "]" and b != '[':
                    return False
                if c == "}" and b != '{':
                    return False
            
        if len(a) != 0:
            return False
        return True

