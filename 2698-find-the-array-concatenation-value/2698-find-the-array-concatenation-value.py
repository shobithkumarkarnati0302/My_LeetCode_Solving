class Solution(object):
    def findTheArrayConcVal(self, nums):
        left, right = 0, len(nums) - 1
        total = 0

        while left <= right:
            if left == right:
                total += nums[left]
            else:
                total += int(str(nums[left]) + str(nums[right]))
            left += 1
            right -= 1

        return total
