class Solution(object):
    def isValid(self, word):
        if len(word) < 3:
            return False

        is_vowel = is_consonant = False
        vowel_set = set("aeiouAEIOU")
        for c in word:
            if not c.isalnum():
                return False
            if c.isalpha():
                if c in vowel_set:
                    is_vowel = True
                else:
                    is_consonant = True
        return is_vowel and is_consonant