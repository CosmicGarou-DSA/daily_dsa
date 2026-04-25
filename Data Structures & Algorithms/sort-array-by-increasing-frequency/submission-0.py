class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        
        def customsort(x):
            return(count[x], -x)
        
        return sorted(nums, key = customsort)