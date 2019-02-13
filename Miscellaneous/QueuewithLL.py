'''Implement a Queue with a Linked List.In this implementation,we will mainatain 
a head and a tail reference as in a queue,we add elements from the back and delete 
elements from the front.Rest Of the Operations can be used from Our Implementation of a
Stack Usinga Linekd List'''

# Base Class

class LinkedQueue:

    # Single Instance of an Element in a Linekd List

    class Node:
        def __init__(self,element,next):
            self.element=element
            self.next=next

    def __init__(self):
        self.head=None
        self.tail=None
        self.size=0

    # Get No Of elemnts in a Queue
    def getSize(self):
        return self.size

    # Get The First Element Of the Queue
    def getHead(self):
        return self.head.element

    # Get the Last Element of the Queue
    def getTail(self):
        return self.tail.element

    # Get All the Elements of the Queue
    def getAll(self):
        base_element=self.head

        return_op=[]

        while base_element!=None:
            return_op.append(base_element.element)
            base_element=base_element.next

        return "".join(str(e) for e in return_op)
    
    #Insert an element at the back of the Queue.
    #Create a New Node,assign the next of the tail to this element.Then asssign tail as the new node 
    def PushOne(self,element):
        newNode=LinkedQueue.Node(element,None)

        currentSize=self.getSize()

        if currentSize==0:
            # First Insert.Head and Tail Reffer to the same node

            self.head=newNode
            self.tail=newNode

            self.head.next=self.tail
            self.size+=1

        else:
            # Tail and head exist separately

            self.tail.next=newNode
            self.tail=newNode
            self.size+=1

    #Delete an element from the front of the Queue.
    #Create a New Node,assign the next of the new node to the head.Then asssign head as the new node
    def DeleteFront(self):
        if self.size==0:
            print("Empty queue.Cannot Delete")
            self.tail=None
        else:
            returnElement=self.head.element
            self.head=self.head.next
            self.size-=1

        return returnElement

#Test Linked Queue.Working Well

testing=LinkedQueue()
testing.PushOne(2)
testing.PushOne(3)
print(testing.getAll())
print(testing.getHead())
print(testing.getTail())
print(testing.getSize())
testing.PushOne(6)
testing.PushOne(9)
print(testing.DeleteFront())
print(testing.DeleteFront())
print(testing.getAll())


