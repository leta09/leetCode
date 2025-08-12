class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        res = []
        sorted_nums = sorted(nums)
        for i in range(len(nums)):
            res.append(sorted_nums.index(nums[i]))
        return res