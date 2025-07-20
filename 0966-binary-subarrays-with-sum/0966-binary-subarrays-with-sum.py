class Solution(object):
    def numSubarraysWithSum(self, nums, goal):

        def ans(goal):
            if goal < 0:
                return 0
            
            left,count,total = 0,0,0

            for right in range(len(nums)):
                total += nums[right]
                while total > goal:
                    total -= nums[left]
                    left += 1
                count += right-left+1
            
            return count
        
        return ans(goal) - ans(goal-1)