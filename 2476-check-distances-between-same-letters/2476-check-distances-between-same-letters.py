class Solution(object):
    def checkDistances(self, s, distance):

        pos = {}
        
        for i, char in enumerate(s):
            if char in pos:
                first_index = pos[char]
                actual_dis = i - first_index - 1
                required_dis = distance[ord(char) - ord('a')]
                
                if actual_dis != required_dis:
                    return False
            else:
                pos[char] = i
                
        return True