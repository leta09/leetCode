class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:

        lower = [ele for ele in nums if ele < pivot]

        equal = [ele for ele in nums if ele == pivot]

        greater = [ele for ele in nums if ele > pivot]

        return lower + equal + greater