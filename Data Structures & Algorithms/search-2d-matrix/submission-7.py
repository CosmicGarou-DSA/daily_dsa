class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat = [ch for row in matrix for ch in row]

        l , h = 0 , len(flat) - 1

        
        while l <= h:
                
            m = (l + h) // 2

            if flat[m] == target:
                return True

            elif flat[m] > target:
                h = m - 1

            elif flat[m] < target:
                l = m + 1

        return False
