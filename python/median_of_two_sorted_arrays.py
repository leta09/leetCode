import math
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = nums1 + nums2
        sorted_n = sorted(n)
        le = len(sorted_n)
        if le % 2 == 0:
            return (sorted_n[math.floor(le/2)-1] + sorted_n[math.floor(le/2)])/2
        elif le%2 !=0:
            return sorted_n[math.floor(le/2)]
