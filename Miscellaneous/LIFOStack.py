'''Classs to perform the operations of a stack.
We are using the adapter patten which uses functions of a differnt class
to map to operations in out stack.Like when we do push an element into the stack,what we
can do in pythin is call the append method since it appends the value to the end of the list.
Simillarly we can use the pop method to delete an elemen from the top of the stack.
'''

class LIFOStack():
    def __init__(self):
        self.data=[]
        self.length=0

    def push(self,val):
        self.data.append(val)
        self.length+=1

    def _pop(self):
        if self.length!=0:
            _return=self.data.pop()
            self.length-=1
            return _return

        else:
            return "Stack is Empty.Cannot pop"

    def getlength(self):
        return self.length

    def getTop(self):

        if self.length!=0:
            return self.data[-1]
        
        else:
            return "Stack is Empty.Cannot Return Top"

    def getItems(self):
        return "".join(str(self.data[e]) for e in range(self.getlength()-1,-1,-1))

# Stack Test.Working For Inputs Properly

test=LIFOStack()

test.push(2)
test.push(6)
print(test.getlength())
test._pop()
test._pop()
test._pop()
print(test.getlength())
print(test.getItems())
test.push(5)
test.push(1)
test.push(6)
abc=test.getItems()
print(abc)