class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()
        count = 0
        for i in range(len(s) -1, -1, -1):
            if s[i] == " ":
                break
            count += 1
        return count 