class Solution(object):
    def maximumGap(self, nums):
        ans = 0
        nums.sort()

        for i in range(len(nums)-1):
            ans = max(ans,nums[i+1]-nums[i])

        return ans