class Solution(object):
    def findTheDifference(self, s, t):
        s_list = list(s)
        t_list = list(t)
        
        for i in s_list:
            if i in t_list:
                t_list.remove(i)
        
        return "".join(t_list)