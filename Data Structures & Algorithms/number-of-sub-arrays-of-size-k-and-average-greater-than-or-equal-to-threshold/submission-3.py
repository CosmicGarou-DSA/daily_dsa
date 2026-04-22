class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count,l=0,0
        r=k-1
        n=len(arr)
        while l <= r and r < n:
            avg=sum(arr[l:r+1])/k
            if avg >= threshold:
                count+=1
            l+=1
            r+=1

        return count