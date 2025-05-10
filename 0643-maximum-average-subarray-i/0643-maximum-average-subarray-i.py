class Solution:
    def findMaxAverage(self, nums, k):
        Sum = 0
        for i in range(0, k):
            Sum += nums[i]
            
        maxSum = Sum
        for j in range(k, len(nums)):
            Sum += nums[j]
            Sum -= nums[j - k]
            maxSum = max(maxSum,Sum)
        return float(maxSum) / k