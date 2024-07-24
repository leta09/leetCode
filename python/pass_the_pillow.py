class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        time = time % (2 * (n - 1))
        print(time)
        if time <= n - 1:
            return time  + 1
        if time > n - 1:
            return abs(n - (time - (n - 1)))