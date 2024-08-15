class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = []
        ten = []
        twenty = []
        res = []
        if bills[0] != 5:
            return False

        for i in bills:
            if i == 5:
                five.append(i)
                res.append(True)
            if i == 10 and len(five) > 0:
                ten.append(i)
                del five[0]
                res.append(True)
            if i == 20:
                if len(five) == 0 :
                    return False
                if len(ten) >0 and len(five)>0:
                    del ten[0]
                    del five[0]
                    twenty.append(i)
                    res.append(True)
                elif len(ten) == 0 and len(five)>=3:
                    del five[0]
                    del five[0]
                    del five[0]
                    twenty.append(i)
                    res.append(True)
                else:
                    res.append(False)
        
        return all(res)