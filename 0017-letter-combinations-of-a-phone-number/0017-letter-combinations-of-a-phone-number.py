from itertools import product

class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        nums = {
            '2' : 'abc',
            '3' : 'def',
            '4' : 'ghi',
            '5' : 'jkl',
            '6' : 'mno',
            '7' : 'pqrs',
            '8' : 'tuv',
            '9' : 'wxyz' 
        }

        arr = [nums[d] for d in digits]

        combos = product(*arr)

        return [''.join(c) for c in combos]
