class Solution(object):
    def diagonalSum(self, mat):
        res = 0
        for i in range(len(mat)):
            res += mat[i][i]
            res += mat[i][len(mat)-1-i]
        
        if len(mat)%2 == 1:
            res -= mat[len(mat)//2][len(mat)//2]

        return res


        