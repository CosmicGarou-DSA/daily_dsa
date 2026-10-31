class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        res = [[1]]
        prev = [1]

        for i in range(numRows - 1):
            curr = [1]
            for j in range(len(prev) - 1):
                curr.append(prev[j] + prev[j+1])
            curr.append(1)
            prev = curr
            res.append(curr)

        return res