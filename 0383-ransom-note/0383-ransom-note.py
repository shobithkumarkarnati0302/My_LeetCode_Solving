class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        ransomlst = list(ransomNote)

        for i in magazine:
            if i in ransomlst:
                ransomlst.remove(i)
        
        return len(ransomlst) == 0
