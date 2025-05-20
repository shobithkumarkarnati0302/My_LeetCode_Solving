class Solution(object):
    def setZeroes(self, matrix):
        m,n = len(matrix),len(matrix[0])
        row_lst = set()
        col_lst = set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row_lst.add(i)
                    col_lst.add(j)
        
        for i in range(m):
            for j in range(n):
                if i in row_lst or j in col_lst:
                    matrix[i][j] = 0
