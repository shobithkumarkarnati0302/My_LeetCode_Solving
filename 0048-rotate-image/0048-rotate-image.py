class Solution:
    def rotate(self, matrix):
        # Determine the size of the matrix
        size = len(matrix)

        # Perform a vertical flip of the matrix
        for i in range(size >> 1):  # size >> 1 is a faster way to do size // 2
            for j in range(size):
                # Swap the top and bottom elements in the column
                matrix[i][j], matrix[size - i - 1][j] = matrix[size - i - 1][j], matrix[i][j]

        # Perform a diagonal flip of the matrix, which is equivalent
        # to transposing the matrix
        for i in range(size):
            for j in range(i):
                # Swap the elements across the diagonal
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]