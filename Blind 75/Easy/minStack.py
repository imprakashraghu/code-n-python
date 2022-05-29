#Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

#Implement the MinStack class:

# MinStack() initializes the stack object.
#void push(int val) pushes the element val onto the stack.
#void pop() removes the element on the top of the stack.
#int top() gets the top element of the stack.
#int getMin() retrieves the minimum element in the stack.

#Input
#["MinStack","push","push","push","getMin","pop","top","getMin"]
#[[],[-2],[0],[-3],[],[],[],[]]

#Output
#[null,null,null,null,-3,null,0,-2]


class MinStack:

    def __init__(self):
      self.stack = []
      
    def push(self, val: int) -> None:
      self.stack.append(val)

    def pop(self) -> None:
      self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
      return min(self.stack)