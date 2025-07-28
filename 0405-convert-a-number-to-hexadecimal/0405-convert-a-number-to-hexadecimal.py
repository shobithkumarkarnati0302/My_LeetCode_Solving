class Solution(object):
    def toHex(self, num):
        hexdigits = "0123456789abcdef"
        ans = ""
        if num == 0:
            return "0"

        if num < 0:
            num += 2**32

        while num:
            mod = num % 16
            if mod > 9:
                ans += hexdigits[mod]
            else:
                ans += str(mod)
        
            num = num//16

        return ans[::-1]

        