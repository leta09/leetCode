def restoreMatrix(rowSum, colSum):       
        rows = []
        col = []
        t = 0
        #min_num = min([min(rowSum), min(colSum)])
        min_num_r = min(rowSum)
        min_num_c = min(colSum)
        for i in rowSum:
            t = i - min_num_r
            rows.append(t)
            print(rows)
        # for i in colSum: 
        #     t = i - min_num
        #     col.append(t)

        #return [rows, col]

print(restoreMatrix([3,8],[4,7]))