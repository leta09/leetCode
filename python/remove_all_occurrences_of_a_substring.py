class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            ind = s.find(part)
            s = s[:ind] + s[(ind + len(part)):]
        return s