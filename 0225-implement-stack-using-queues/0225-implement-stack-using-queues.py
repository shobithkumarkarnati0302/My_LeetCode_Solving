from _collections import deque

class MyStack(object):

    def __init__(self):
        self.s1 = deque()
        self.s2 = deque()

    def push(self, x):
        self.s2.append(x)
        while self.s1:
            self.s2.append(self.s1.popleft())
        self.s1, self.s2 = self.s2, self.s1

    def pop(self):
        if self.s1:
            return self.s1.popleft() 

    def top(self):
        if self.s1:
            return self.s1[0]
        return None

    def empty(self):
        return not self.s1



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()