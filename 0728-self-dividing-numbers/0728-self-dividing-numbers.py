class Solution(object):
    def selfDividingNumbers(self, left, right):
        res = []
        for num in range(left, right + 1):
            flag = True
          
            for digit_str in str(num):
                digit = int(digit_str)
              
                if digit == 0 or num % digit != 0:
                    flag = False
                    break
          
            if flag:
                res.append(num)
      
        return res