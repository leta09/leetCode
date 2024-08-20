class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        sm = arrays[0][0]
        bg = arrays[0][-1]
        dist = 0
        for i in range(1, len(arrays)):
            dist = max(dist, abs(bg - arrays[i][0]) ,abs(arrays[i][-1] - sm))
            sm = min(arrays[i][0], sm)
            bg = max(arrays[i][-1], bg)
        return dist