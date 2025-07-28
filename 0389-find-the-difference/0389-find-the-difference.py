class Solution(object):
    def findTheDifference(self, s, t):
        # s_list = list(s)
        # t_list = list(t)
        
        # for i in s_list:
        #     if i in t_list:
        #         t_list.remove(i)
        
        # return "".join(t_list)

        s_ans = 0
        t_ans = 0

        for i in s:
            s_ans += ord(i)
        for j in t:
            t_ans += ord(j)

        return chr(t_ans-s_ans)