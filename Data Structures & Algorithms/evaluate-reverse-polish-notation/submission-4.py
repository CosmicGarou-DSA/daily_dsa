class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        top = -1
        for ch in tokens:
            if ch.lstrip('-').isdigit():
                stack.append(int(ch))
                top+=1
            else:
                if ch == '+':
                    a = stack.pop()
                    b = stack.pop()
                    res = b + a
                    top-=1
                    stack.append(res)

                elif ch == '-':
                    a = stack.pop()
                    b = stack.pop()
                    res = b - a
                    top-=1
                    stack.append(res)
        
                elif ch == '*':
                    a = stack.pop()
                    b = stack.pop()
                    res = b * a
                    top-=1
                    stack.append(res)
            
                elif ch == '/':
                    a = stack.pop()
                    b = stack.pop()
                    res = int(b / a)
                    top-=1
                    stack.append(res)
        return stack[top]