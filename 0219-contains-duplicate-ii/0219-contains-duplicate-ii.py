class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        d = {}
        for i, x in enumerate(nums):
            if x in d and i - d[x] <= k:
                return True
            d[x] = i
        return False
        