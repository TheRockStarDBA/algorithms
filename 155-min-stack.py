""" 155. Min Stack - Easy
topic: stack, design
related:    Sliding Window Maximum - Hard
            Max Stack - Easy

Design a stack that supports push, pop, top, and retrieving the minimum element
in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2. """


# Time:  O(n)
# Space: O(n)
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if not self.minStack:
            self.minStack.append(x)
        else:
            if x <= self.minStack[-1]:
                self.minStack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            if self.minStack[-1] == self.stack[-1]:
                self.minStack.pop()
            self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.minStack:
            return self.minStack[-1]


import sys


class MinStack2(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min = sys.maxsize
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if x <= self.min:
            self.stack.append(self.min)
            self.min = x

        self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            if self.stack.pop() == self.min:
                self.min = self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
if __name__ == "__main__":
    testStack = MinStack()
    testStack.push(4)
    testStack.push(5)
    testStack.push(1)
    testStack.push(3)
    testStack.pop()
    testTop = testStack.top()
    testMin = testStack.getMin()
    print(testMin, testTop)