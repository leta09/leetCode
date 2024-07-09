class Solution:
    def minDifference(self, nums: List[int]) -> int:
        sorted_nums= sorted(nums)
        res = []
        if len(nums) <=4:
            return 0
        else:
            #from the start
            a = sorted_nums[3:]
            #from the end
            b = sorted_nums[:len(sorted_nums)-3]
            #two start one end
            c = sorted_nums[2:len(sorted_nums)-1] 
            # one start two end
            d = sorted_nums[1:len(sorted_nums)-2] 

            res.append(max(a)-min(a))
            res.append(max(b)-min(b))
            res.append(max(c)-min(c))
            res.append(max(d)-min(d))
            return min(res)