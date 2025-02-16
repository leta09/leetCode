class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        temp = []
        a = []
        arr = [(nums[i-1],nums[i])for i in range(len(nums))]
        if len(arr) == 1:
            return True
        else:
            arr.pop(0)
            for i in arr:
                temp = []
                for j in i:
                    if j % 2 == 0:
                        temp.append(True)
                    else:
                        temp.append(False)
                
                a.append(temp)
            

            for i in a:
                for j in range(len(i)):
                    if i[0] == True and i[1] == True:
                        return False
                    if i[0] == False and i[1] == False:
                        return False
                    
            return True
                    