class Solution(object):
    def removeDuplicates(self, nums):
        dupli = {}
        for i in nums:
            if i in dupli:
                dupli[i] += 1
            else:
                dupli[i] = 1
        
        res = []
        for key in sorted(dupli):  
            count = min(2, dupli[key]) 
            res.extend([key] * count)
            
        for i in range(len(res)):
            nums[i] = res[i]

        return len(res)