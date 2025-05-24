class Solution(object):
    def minimumDifference(self, nums, k):
        nums.sort()
        min_diff = float('inf')
        for i in range(len(nums) - k + 1):
            current_diff = nums[i + k - 1] - nums[i]
            if current_diff < min_diff:
                min_diff = current_diff
        return min_diff