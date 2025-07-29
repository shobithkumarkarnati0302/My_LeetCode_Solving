class Solution(object):
    def addMinimum(self, word):
        k = 1
        for i in range(1, len(word)):
            if word[i] <= word[i-1]:
                k += 1
        return (k * 3) - len(word)