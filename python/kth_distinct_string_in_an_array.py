class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        t = []
        for i in arr:
            if arr.count(i) == 1:
                t.append(i)

        if len(t) < k:
            return ""
        return t[k-1]