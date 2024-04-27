class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = dict()
        li = list(set(nums))
        for i in li:
            dic[i] = nums.count(i)

        for k,v in dic.items():
            if v > int(len(nums)/2):
                return k