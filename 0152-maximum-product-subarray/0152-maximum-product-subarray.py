class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0
        
        max_now = nums[0]
        min_now = nums[0]
        result = nums[0]
        
        for i in range(1, len(nums)):
            num = nums[i]
            temp_max = max(num, num * max_now, num * min_now)
            temp_min = min(num, num * max_now, num * min_now)
            
            max_now = temp_max
            min_now = temp_min
            
            result = max(result, max_now)
        
        return result