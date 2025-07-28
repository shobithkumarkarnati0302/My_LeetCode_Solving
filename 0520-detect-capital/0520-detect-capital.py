class Solution(object):
    def detectCapitalUse(self, word):
        word1 = word.upper()
        word2 = word.lower()
        word3 = word.capitalize()

        return word == word1 or word == word2 or word == word3
        