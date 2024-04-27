class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        li = s.strip().split(" ")
        w = li[-1]
        return len(w)