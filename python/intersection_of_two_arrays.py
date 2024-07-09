class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        j = 0
        i = 0
        snums1 = sorted(nums1)
        snums2 = sorted(nums2)
        while i < len(snums1) and j < len(snums2):
            if snums1[i] < snums2[j]:
                i = i + 1
            elif snums2[j] < snums1[i]:
                j = j + 1
            else:
                res.append(snums1[i])
                i = i +1
                j = j + 1
        return res