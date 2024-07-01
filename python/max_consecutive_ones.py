class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        t = []
        c = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                c+=1
              
            if nums[i] !=1 or len(nums)-1 == i:
                t.append(c)
                c = 0
        return max(t)