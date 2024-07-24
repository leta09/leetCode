
def duplicateZeros(arr):
        """
        Do not return anything, modify arr in-place instead.
        """
       
        temp = arr
        arr = []
        
        for i in range(len(temp)):
            if temp[i] !=0:
                arr.append(temp[i])
            else:
                arr.append(0) 
                arr.append(0) 

        print(arr)
        diff = len(arr) - len(temp)
        print(diff)
        while diff >0:
             del arr[-diff]
             diff = diff - 1
        print(arr)
        # len_arr = len(arr)
        # pos = []
        # count = 0
        # for i in arr:
        #      if i == 0:
        #         count +=1
        # print(count)
        # arr = arr + arr[-count:]
        # print(arr)
        # for i in range(len(arr)):
        #     if arr[i] == 0:
        #         pos.append(i)
        # print(pos)
        # for i in pos:
        #        arr.insert(i+1, 0)
               
        # print(arr)
        # while count > 0:
        #     del arr[-count]
        #     count=count - 1
            
        # print(arr)

#duplicateZeros([1,0,2,3,0,4,5,0])
duplicateZeros([0,1,7,6,0,2,0,7])