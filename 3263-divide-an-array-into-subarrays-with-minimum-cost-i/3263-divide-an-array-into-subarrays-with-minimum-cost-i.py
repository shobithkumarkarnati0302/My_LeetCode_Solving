class Solution(object):
    def minimumCost(self, nums):
        fixed_cost = nums[0]
        
        remaining_arr = nums[1:]
        
        remaining_arr.sort()
        
        total_cost = fixed_cost + remaining_arr[0] + remaining_arr[1]
        
        return total_cost