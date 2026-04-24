class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set([ch for ch in nums1 if ch in nums2]))
        