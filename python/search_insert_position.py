class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        h = len(nums) - 1
        l = 0
        for i in range(len(nums)):
            if target == nums[i]:
                return  i
        
        while h >= l:
            m = (l+h)//2
            if nums[m]>target:
                h = m -1
            elif nums[m]<target:
                l = m + 1
        if nums[m]> target:
            return m
        else: return m + 1