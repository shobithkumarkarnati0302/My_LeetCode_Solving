class Solution(object):
    def minCuttingCost(self, n, m, k):
        diff1 = 0
        diff2 = 0
        ans = 0

        if n > k:
            diff1 = n-k
        if m > k:
            diff2 = m-k
        ans = k*diff1 + k*diff2

        return ans
