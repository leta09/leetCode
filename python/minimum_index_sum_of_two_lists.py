class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common = []
        indexes = []
        indexes_sum = []
        res = []
        for i in list1:
            if i in list2:
                common.append(i)
        if len(common) == 1:
            return common 
        else:
            for i in common:
                indexes.append([list1.index(i), list2.index(i)])
                indexes_sum.append(sum([list1.index(i), list2.index(i)]))
                mi = min(indexes_sum)
            for i in range(len(indexes)):
                if sum(indexes[i]) == mi:
                    res.append(common[i])
            return list(set(res))