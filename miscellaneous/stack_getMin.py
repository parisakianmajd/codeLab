# push(x): Push element x onto stack.
# pop(): Removes the element on top of the stack.
# top(): Get the top element.
# getMin(): Retrieve the minimum element in the stack.
import sys

class Stack():
    def __init__(self):
        self.stack = []
        self.minElem = None
    def push(self, x):
        if len(self.stack) == 0:
            self.stack.append(x)
            self.minElem = x
        elif x < self.minElem:
            self.stack.append(2 * x - self.minElem)
            self.minElem = x
        else:
            self.stack.append(x)

    def pop(self):
        if len(self.stack) == 0:
            return -1
        x = self.stack.pop()
        if x < self.minElem:
            self.minElem = 2 * self.minElem - x
        return x

    def peek(self):
        if len(self.stack) == 0:
            return -1
        x = self.stack[-1]
        if x < self.minElem:
            return self.minElem
        return x

    def getMin(self):
        return self.minElem

    
class MinStack:
        
    def __init__(self):
        self.stack = []
        self.minstack = []
        
    def push(self, x):
        if len(self.stack) == 0:
            self.minstack.append(x)
            self.stack.append(x)

        else:
            self.stack.append(x)
            if  x < self.minstack[-1]:
                self.minstack.append(x)  
            else:
                self.minstack.append(self.minstack[-1])  

    def pop(self):
        if len(self.stack) != 0:
            self.stack.pop()
            self.minstack.pop()

    def top(self):
        if len(self.stack) == 0:
            return -1
        x = self.stack[-1]
        return x

    def getMin(self):
        if len(self.minstack) == 0:
            return -1
        return self.minstack[-1]

s = Stack()
s.push(3)
s.push(5)
print "min: " + str(s.getMin())
s.push(2)
s.push(1)
print "min: " + str(s.getMin())
s.pop()
print "min: " + str(s.getMin())
s.pop()
print "peek: " + str(s.peek())
    
