class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dic = dict()
        for i in arr:
            if arr.count(i) == i:
                k = str(i)
                dic[k] = arr.count(i)
        if dic == {}:
            return -1
        else:
            return max(dic.values())