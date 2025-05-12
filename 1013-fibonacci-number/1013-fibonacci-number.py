class Solution(object):
    def fib(self, n):
        a = 0
        b = 1
        for i in range(n):
            res = a+b
            a = b
            b = res
        return a