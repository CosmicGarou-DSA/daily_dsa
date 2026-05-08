class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures) 
        for i , ch in enumerate(temperatures):
            while stack and ch > temperatures[stack[-1]]:
                prev = stack.pop()
                result[prev] = i - prev
            stack.append(i)
        return result