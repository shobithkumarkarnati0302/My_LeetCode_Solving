class Solution(object):
    def matrixReshape(self, mat, r, c):
        m = len(mat)
        n = len(mat[0])

        res = [[0]*c for _ in range(r)]
        x = 0
        y = 0

        if m*n != r*c:
            return mat

        for i in range(m):
            for j in range(n):
                res[x][y] = mat[i][j]
                y += 1
                if y==c:
                    y = 0
                    x += 1
        return res

