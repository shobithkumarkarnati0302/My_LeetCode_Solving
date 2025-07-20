class Solution(object):
    def singleNumber(self, nums):
        mydict = {}
        for i in nums:
            if i in mydict:
                mydict[i] += 1
            else:
                mydict[i] = 1
        
        for i in mydict:
            if mydict[i] == 1:
                return i
                break