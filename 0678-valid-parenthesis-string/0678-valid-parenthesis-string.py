class Solution(object):
    def checkValidString(self, s):
        x = 0
        for c in s:
            if c in '(*':
                x += 1
            elif x:
                x -= 1
            else:
                return False
        x = 0
        for c in s[::-1]:
            if c in '*)':
                x += 1
            elif x:
                x -= 1
            else:
                return False
        return True