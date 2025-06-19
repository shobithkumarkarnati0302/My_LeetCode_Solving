class Solution(object):
    def sortedSquares(self, nums):
        res = list(map(lambda x:x**2,nums))
        res.sort()
        return res