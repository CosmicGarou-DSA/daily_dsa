class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        form = {')':'(',']':'[','}':'{'}
        for ch in s:
            if ch in form:
                if stack and stack[-1] == form[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        return True if not stack else False