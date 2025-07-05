class Solution:
    def divideString(self, s: str, k: int, fill: str):
            num = 0
            res = [s[i:(i+k)] for i in range(0,len(s), k)]

            num = k - len(res[-1])
            if num != 0:
                print(num)
                res[-1] +=  (num*fill)
            return res