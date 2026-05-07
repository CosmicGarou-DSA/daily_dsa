class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ch in asteroids:
            if ch > 0:
                stack.append(ch)
            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(ch):
                    stack.pop()
                if stack and stack[-1] > 0 and stack[-1] == abs(ch):
                    stack.pop()
                elif not stack or stack[-1] < 0:
                    stack.append(ch)
        return stack
