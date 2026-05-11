class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        newpaths = path.split('/')
        for ch in newpaths:
            if ch == '..':
                if stack:
                    stack.pop()
            elif ch != "" and ch!='.':
                stack.append(ch)

        return "/"+"/".join(stack)