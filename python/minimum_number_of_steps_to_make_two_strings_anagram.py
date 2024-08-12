class Solution:
    def minSteps(self, s: str, t: str) -> int:
        r = 0
        for i in set(s):
            if t.count(i) < s.count(i):
                r += (s.count(i) - t.count(i))
        return r