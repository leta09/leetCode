class Solution: 
    def findComplement(self, num: int) -> int:
        res = ""
        binary = bin(num)
       
        for i in binary[2:]:
            if i == "0":
                res = res + "1"
            if i == "1":
                res = res + "0"
        
    
        return int(res, 2)