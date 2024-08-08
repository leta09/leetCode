class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        r = []
        if target not in nums:
            return [-1, -1]
        else:
            for i in range(len(nums)):
                if nums[i] == target:
                    r.append(i)
            return [r[0],r[-1]]