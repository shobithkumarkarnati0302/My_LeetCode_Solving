class Solution(object):
    def maximumGain(self, s, x, y):
    
        if x < y:
            x, y = y, x 
            s = s[::-1] 
        
        score = 0
        
        stack1 = []
        for char in s:
            if char == 'b' and stack1 and stack1[-1] == 'a':
                stack1.pop()
                score += x
            else:
                stack1.append(char)
     
        stack2 = []
        for char in stack1:
            if char == 'a' and stack2 and stack2[-1] == 'b':
                stack2.pop()
                score += y
            else:
                stack2.append(char)

        return score