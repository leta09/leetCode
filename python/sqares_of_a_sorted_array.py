class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        sqr = [i**2 for i in nums]
        return sorted(sqr)