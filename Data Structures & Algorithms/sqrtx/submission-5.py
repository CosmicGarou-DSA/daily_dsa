class Solution:
    def mySqrt(self, x: int) -> int:
        l , h = 0 , x 

        while l <= h:
            
            m = (l + h) // 2

            if (m * m) == x:
                return m

            elif (m * m) > x:
                h = m - 1

            elif (m * m) < x:
                l = m + 1
            
        return h