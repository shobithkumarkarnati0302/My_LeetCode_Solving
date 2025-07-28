class Solution(object):
    def findWords(self, words):
        f_row = "qwertyuiop"
        s_row = "asdfghjkl"
        t_row = "zxcvbnm"

        res = []

        for j in words:
            i = j.lower()
            if set(i).issubset(set(f_row)) or set(i).issubset(set(s_row)) or set(i).issubset(set(t_row)):
                res.append(j)

        return res
        