"""Implementing a Stack With the Help of a Linked List"""
'''0->0->0->0-> A collection fof elements joined together to refer to the next subsequent 
element.In our case,the top of the stack is represented by the head as it's easier to get the first
item in the list(Top of the stack)'''

#Main Class
class LinkedListStack:

    def __init__(self,head,size):
        self.head=None
        self.size=0

    #Sub Class for Node(Objects which are used in a Linked List)

    class Node:
        def __init__(self,element,next):
            self.element=element
            self.next=next

    
    def getSize(self):
        print(self.size)


    '''If size is 0,create an instance of the node class and assign the head to it.
    else create an instance of the node class and then assign the next of the new node to the current head
    and the next of head to our node'''

    def Push(self,element):
        # First Element Insertion
        if self.size==0:
            new_node=LinkedListStack.Node(element,None)
            self.head=new_node
            self.size+=1

        # N'th Element Insertion
        else:
            new_node=LinkedListStack.Node(element,self.head)
            self.head=new_node
            self.size += 1
    
    '''Get the head node first.Make a copy.Then asssing the head to the elemnt being pointed by the head
    and decrement size by one '''

    def Pop(self):
        if self.size!=0:
            returnVal=self.head.element

            self.head=self.head.next
            self.size-=1

        return returnVal

    def getTop(self):
        if self.size!=0:
            return self.head.element

    '''Traverse throughout the List,get each element's element and add it to the list,
    only stop when the current element is none'''

    def getAll(self):
        base_element=self.head

        value_arr=[]

        # print(base_element.element)

        while base_element!=None:
            value_arr.append(base_element.element)
            base_element=base_element.next

        print(value_arr)



# Testing Code.Works Well
NewNode=LinkedListStack(0,0)
NewNode.Push(2)
NewNode.Push(3)
print(NewNode.getTop())
NewNode.getSize()
NewNode.Push(6)
NewNode.getAll()
NewNode.Pop()
NewNode.Pop()
print(NewNode.getTop())
NewNode.getSize()
NewNode.Push(9)
NewNode.getAll()
print(NewNode.getTop())
