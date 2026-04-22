class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        count,l=0,0
        r=k-1
        n=len(arr)
        Sum=sum(arr[l:r+1])
        if Sum / k >= threshold:
            count+=1
        
        for i in range(k, n):
            Sum+=arr[i] - arr[i-k]
            if Sum / k >= threshold:
                count+=1
        return count