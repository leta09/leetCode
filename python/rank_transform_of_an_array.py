class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        rank = dict()
        arr1 = sorted(list(set(arr.copy())))
        if len(arr1) == 1:
            for i in range(len(arr)):
                arr[i] = 1
            return arr
        for i in range(len(arr1)):
            rank[arr1[i]] = i+1

        for i in range(len(arr)):
            arr[i] = rank[arr[i]]
        return arr
        