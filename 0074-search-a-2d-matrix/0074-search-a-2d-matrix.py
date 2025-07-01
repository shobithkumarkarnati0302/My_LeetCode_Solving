class Solution(object):
    def searchMatrix(self, matrix, target):
        found = False
        for i in matrix:
            if target in i:
                found = True

        return found