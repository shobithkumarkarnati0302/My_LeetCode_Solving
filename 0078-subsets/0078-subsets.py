from itertools import combinations

class Solution(object):
    def subsets(self, nums):
        res = []

        for k in range(len(nums) + 1):
            for c in combinations(nums, k):
                res.append(list(c))
                
        return res
