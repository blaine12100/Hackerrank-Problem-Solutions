"""
In this file,we will implement a simple stack using normal list methods to illustrate
how easy it is to maintain a stack.

This stack will support some key operations:
Push:To add an element in the stack.

Pop:To delete and Element from the stack.

Top:Return the current top elemnt of the stack

Size:Current No of Items in the stack

Tested with the Driver Code and Eliminated a Few Bugs.
"""


class Simple_Stack:
    def __init__(self):
        self.simple_stack = []
        self.top = 0
        self.size = 0

    def get_size(self):
        return self.size

    def get_top(self):
        # For getitng the Top if the stack is already empty so we cannot do this.
        if self.isEmpty():
            return False
        return self.simple_stack[self.top]

    def isEmpty(self):
        return self.get_size() == 0

    def push(self, item):

        if self.isEmpty():
            self.simple_stack.append(item)
            self.size += 1

            self.top = 0

        else:
            self.simple_stack.append(item)
            self.size += 1

            self.top += 1

        return True

    def pop(self):
        if self.isEmpty():
            return False
        else:
            # Pop Element at the Last(First Acc to Stack)
            self.simple_stack.pop()
            self.top -= 1
            self.size -= 1
            return True


# Driver_Code

new_stack = Simple_Stack()
new_stack.pop()
new_stack.push(2)
new_stack.get_size()
new_stack.get_top()
new_stack.push(3)
new_stack.pop()
new_stack.get_top()
new_stack.pop()
new_stack.get_top()
new_stack.push(13)
new_stack.push(14)
new_stack.get_top()
