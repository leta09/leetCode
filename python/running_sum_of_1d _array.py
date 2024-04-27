class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []
        temp = 0
        for i in range(len(nums)):
            temp = temp + nums[i]
            res.append(temp)
        return res