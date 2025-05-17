class Solution(object):
    def findMaxK(self, nums):
        ans = -1
        s = set(nums)
        for x in s:
            if -x in s:
                ans = max(ans, x)
        return ans
        