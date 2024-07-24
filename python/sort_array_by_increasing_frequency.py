

class Solution:
  
    def frequencySort(self, nums: List[int]) -> List[int]:
        fr = dict()
        
        for i in nums:
            fr[i] = nums.count(i)
        
        nums.sort(key=lambda x:(fr[x], -x))
        return nums