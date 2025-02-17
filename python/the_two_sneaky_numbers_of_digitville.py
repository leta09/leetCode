class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        

        res = [i for i in nums if nums.count(i) > 1]
        return list(set(res))