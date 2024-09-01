class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        res = []
        sorted_n = sorted(nums)
        for i in range(len(sorted_n)):
            if target == sorted_n[i]:
                res.append(i)
        return res