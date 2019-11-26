class SpiralMatrix:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        row_begin = 0
        row_end = len(matrix)
        column_begin = 0
        column_end = len(matrix[0])
        res = []

        while row_end > row_begin and column_end > column_begin:
            for i in range(column_begin, column_end):
                res.append(matrix[row_begin][i])
            for j in range(row_begin+1,row_end-1):
                res.append(matrix[j][column_end-1])

            if row_end != row_begin+1:
                for i in range(column_end-1,column_begin-1,-1):
                    res.append(matrix[row_end-1][i])
            if column_begin != column_end-1:
                for j in range(row_end-2,row_begin,-1):
                    res.append(matrix[j][column_begin])
            row_begin += 1
            row_end -=1
            column_begin += 1
            column_end -=1
        return res
