class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        st = ""
        for i in digits:
            st = st + str(i)
        n = str(int(st) + 1)
        return [int(i) for i in n]