class Solution(object):
    def checkString(self, s):

        for i in range(len(s)):
            if s[i] == 'a':
                continue
            if s[i] == 'b':
                if 'a' in s[i:]:
                    return False
        return True