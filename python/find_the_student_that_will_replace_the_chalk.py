class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
       tot = sum(chalk)
       rem = k % tot
       for i in range(len(chalk)):
            rem = rem - chalk[i]
            if rem < 0:
                return i