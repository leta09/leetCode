class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        c = 0
        st = [str(i) for i in nums]
        digits = [ len(i) for i in st]
        for i in digits:
            if i % 2 == 0: 
                c +=1
        return c