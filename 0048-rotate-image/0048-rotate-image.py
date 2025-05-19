class Solution:
    def rotate(self, matrix):
        size = len(matrix)

        for i in range(size >> 1):  
            for j in range(size):
                matrix[i][j], matrix[size - i - 1][j] = matrix[size - i - 1][j], matrix[i][j]

        for i in range(size):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]