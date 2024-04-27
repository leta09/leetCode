class Solution:
    def scoreOfString(self, s: str) -> int:
        su = 0
        val = [ ord(i) for i in s]
        zipped = list(zip(val, val[1:]))
        for i, j  in zipped:
            su = su + abs(i - j)
        return su

