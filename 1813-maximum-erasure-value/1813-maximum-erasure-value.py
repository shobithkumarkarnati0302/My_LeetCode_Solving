class Solution(object):
    def maximumUniqueSubarray(self, nums):
        res,sco = 0,0
        seen = set()
        l = 0
        for r,num in enumerate(nums):
            while num in seen:
                sco -= nums[l]
                seen.remove(nums[l])
                l += 1
            seen.add(nums[r])
            sco += nums[r]
            res = max(res,sco)

        return res
        