class Solution:
    def countSeniors(self, details: List[str]) -> int:
        ages = []
        count = 0
        for i in details:
            ages.append(i[11:13])
       
        for i in ages:
            if int(i) > 60:
                count+=1
        return count