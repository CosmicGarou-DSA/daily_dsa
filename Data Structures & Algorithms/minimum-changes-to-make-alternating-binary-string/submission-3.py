class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        count1,count2=0,0
        a="".join('0' if i%2==0 else '1' for i in range(n))
        b="".join('1' if i%2==0 else '0' for i in range(n))

        for i in range(n):

            if s[i]!=a[i]:
                count1+=1
    
            if s[i]!=b[i]:
                count2+=1
    
        return min(count1,count2)