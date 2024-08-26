class Solution:
    def reverse(self, x: int) -> int:
        n = 0
        if x < 0:
            n = "-" + str(abs(x))[::-1]
            x = int(n)
            if len(bin(x)[2:]) <=32:
                return x
            else:
                return 0
        else:
            x = int(str(abs(x))[::-1])
            if len(bin(x)[2:]) <=32-1:
                return x
            else:
                return 0