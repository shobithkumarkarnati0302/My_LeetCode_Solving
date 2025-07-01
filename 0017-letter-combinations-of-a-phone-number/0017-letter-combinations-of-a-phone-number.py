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

        arr = []
        for digit in digits:
            arr.append(nums[digit])

        combos = product(*arr)

        return [''.join(c) for c in combos]
