class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:

        last = None
        if k == 0:
            return True
        for ind, num in enumerate(nums):
            if num == 1:
                if last != None and ind - last <= k:
                    return False
                last = ind
        return True