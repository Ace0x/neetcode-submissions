class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            
            if i == '+':
                a = int(stack.pop(-1))
                b = int(stack.pop(-1))
                i = b + a
                print(b,'+',a)
                pass
            if i == '-':
                a = int(stack.pop(-1))
                b = int(stack.pop(-1))
                i = b - a
                print(b,'-',a)
                pass
            if i == '*':
                a = int(stack.pop(-1))
                b = int(stack.pop(-1))
                i = b * a
                print(b,'*',a)
                pass
            if i == '/':
                a = int(stack.pop(-1))
                b = int(stack.pop(-1))
                i = b / a
                print(b,'/',a)
                pass
            stack.append(i)
        return int(stack[-1])