class Solution(object):
    def setZeroes(self, matrix):
        m,n = len(matrix),len(matrix[0])
        row = [False]*m
        col = [False]*n

        iszero = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    row[i] = col[j] = True
        
        for i in range(m):
            for j in range(n):
                if row[i] or col[j]:
                    matrix[i][j] = 0