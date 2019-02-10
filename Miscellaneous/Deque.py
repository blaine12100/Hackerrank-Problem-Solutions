"""Double Ended Queue.A double ended queue basically allows for the insertion and 
deletion operations to be done at both the beginneing and at the end of the queue.It 
is very simillar to a normal queue.An example where a Deque can be used is when a
restaurant has to maintain a waiting list for customers.Customers can either leave from the 
front of the queue or the last person can go and leave the queue"""

class NormalDeque:
    def __init__(self):
        self._data=[]
        self.head=0
        self.tail=0
        self.length=0

    def GetFirst(self):
        return self.head

    def GetLast(self):
        return self.tail

    def AddFirst(self,value):
        if self.length==0:
            self._data.append(value)
            self.head=self._data[0]
            self.tail=self._data[0]
            self.length+=1
        else:
            self._data.insert(0,value)
            self.head = self._data[0]
            self.length+=1

    def AddLast(self,value):
        self._data.append(value)
        self.tail=self._data[-1]
        self.length+=1

    def DeleleFirst(self):
        if self.CheckEmpty():
            return "Empty Queue.Cannot Delete"
        else:
            self._data.pop(0)
            self.length-=1

    def DeleleLast(self):
        if self.CheckEmpty():
            return "Empty Queue.Cannot Delete"
        else:
            print(self._data[-1])
            self._data.pop()
            self.length -= 1

    def GetAll(self):
        if self.CheckEmpty():
            return "Queue empty.Nothing to Print"
        else:
            return " ".join(str(e) for e in self._data)

    def CheckEmpty(self):
        print(self.Getlength())
        return self.length==0

    def Getlength(self):
        return self.length


# Testing

test=NormalDeque()

print(test.DeleleFirst())
print(test.DeleleLast())

test.AddFirst(1)
test.AddFirst(2)
print(test.GetAll())
print(test.Getlength())
test.AddLast(4)
test.AddLast(5)
print(test.GetAll())
test.DeleleFirst()
test.DeleleLast()
print(test.GetAll())
print(test.Getlength())
