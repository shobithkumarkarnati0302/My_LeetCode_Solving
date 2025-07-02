class Solution(object):
    def convertToTitle(self, columnNumber):
        res = ""
        while columnNumber > 0:
            rem = (columnNumber - 1) % 26
            res += chr(65 + rem)
            columnNumber = (columnNumber - 1) // 26
        return res[::-1]