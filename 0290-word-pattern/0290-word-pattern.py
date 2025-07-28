class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split()
    
        if len(pattern) != len(words):
            return False

        pairings = zip(pattern, words)
        unique_pairings = set(pairings)

        unique_chars = set(pattern)
        unique_words = set(words)

        return len(unique_pairings) == len(unique_chars) == len(unique_words)