class Solution(object):
    def setZeroes(self, matrix):
        m,n = len(matrix),len(matrix[0])
        ans = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                ans[i][j] = matrix[i][j]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(n):
                        ans[i][k] = 0
                    for l in range(m):
                        ans[l][j] = 0

        for i in range(m):
            for j in range(n):
                matrix[i][j] = ans[i][j]
        
