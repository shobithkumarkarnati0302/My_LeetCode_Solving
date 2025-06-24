class Solution(object):
    def maximumProduct(self, nums):
        nums1 = nums

        if len(nums) == 3:
            return reduce(lambda x, y: x * y, nums)
        
        max1 = max(nums)
        nums.remove(max1)
        max2 = max(nums)
        nums.remove(max2)
        max3 = max(nums)
        product1 = max1*max2*max3

        min1 = min(nums1)
        nums1.remove(min1)
        min2 = min(nums1)

        product2 = min1*min2*max1

        return max(product1,product2)



        