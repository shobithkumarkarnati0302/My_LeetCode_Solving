class Solution(object):
    def rotate(self, nums, k):
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]

        '''
        here nums[:] is used because we need to sollve it in O(1) space
        and nums[:] modifies the 
        '''