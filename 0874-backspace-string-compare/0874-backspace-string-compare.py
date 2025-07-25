class Solution(object):
    def backspaceCompare(self, s, t):
        s1 = []
        s2 = []

        for i in s:
            if i == "#" and s1:
                s1.pop()
            elif i != "#":
                s1.append(i)
        
        for j in t:
            if j == "#" and s2:
                s2.pop()
            elif j != "#":
                s2.append(j)

        return s1 == s2