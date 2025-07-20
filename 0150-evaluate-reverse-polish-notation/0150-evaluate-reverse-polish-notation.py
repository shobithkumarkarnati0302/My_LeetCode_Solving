class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for token in tokens:
            if token in "+-*/":
                b = stack.pop()
                a = stack.pop()

                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    stack.append(int(float(a) / b)) 
            else:
                stack.append(int(token))
        
        return stack[0]