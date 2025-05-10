import sys
class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0
        right = 0
        currsum = 0
        minlen = sys.maxsize

        for right in range(len(nums)):
            currsum += nums[right]
            while currsum >= target:
                if right-left+1 < minlen:
                    minlen = right-left+1
                currsum -= nums[left]
                left += 1
        if minlen != sys.maxsize:
            return minlen
        else:
            return 0