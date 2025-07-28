class Solution(object):
    def repeatedSubstringPattern(self, s):
        s_modified = s+s
        s_modified = s_modified[1:-1]

        if s in s_modified:
            return True 
        else:
            return False 
