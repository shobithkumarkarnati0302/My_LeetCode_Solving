class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        answer = [1] * n

        start = 1
        for i in range(n):
            answer[i] = start
            start *= nums[i]

        end = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= end
            end *= nums[i]

        return answer
