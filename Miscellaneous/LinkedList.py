'''Creating a Singly Linked List which works correctly
This contains various parts which have been used from Queue with LL and stack with LL'''

class LinkedList:

    def __init__(self,head,size):
        self.head=None
        self.size=0


    '''Inner Class to Represent a Instance of a List Element'''
    class Node:
        def __init__(self,element,next):
            self.element=element
            self.next=next

    # Get First Element of the LL
    def getHead(self):
        return self.head

    # Get Size of the LL
    def getSize(self):
        return self.size

    #Check if LL is empty
    def isEmpty(self):
        return self.size==0

    # Get All Elements of the LL
    def getAll(self):
        base_element=self.head
        temp_list=[]

        while base_element!=None:
            temp_list.append(base_element.element)
            base_element=base_element.next
            
        return "->".join(str(e) for e in temp_list)

    # Insert the elment at the start of the LL
    def insertFront(self,value):

        # First Element Insertion
        if self.size == 0:
            new_node = LinkedList.Node(value, None)
            self.head = new_node
            self.size += 1

        # N'th Element Insertion
        else:
            new_node = LinkedList.Node(value, self.head)
            self.head = new_node
            self.size += 1

    # Insert the elment at the last position of the LL
    def insertLast(self,value):
        if self.isEmpty():
            newNode = LinkedList.Node(value, None)
            self.head = newNode
            self.size+1

        else:
            base_element = self.head
            while base_element.next != None:
                base_element = base_element.next
        
            newNode = LinkedList.Node(value,None)
            base_element.next = newNode
            self.size += 1

    # Delete the elment at the start of the LL
    def deleteFirst(self):
        if self.isEmpty():
            print("Empty List,Cannot Delete")
        else:
            returnelement=self.head
            self.head=self.head.next
            self.size-=1

            return returnelement.element

    #Delete the elment at the last position of the LL
    def deleteLast(self):
        if self.isEmpty():
            print("Empty List,Cannot Delete")

        else:
            base_element=self.head
            next_element=base_element.next

            returnelement=next_element.element

            while next_element.next!=None:
                base_element=next_element
                next_element=next_element.next

            base_element.next=None
            self.size-=1

            return returnelement

    # Insert the elment at a specifed position of the LL
    def insertMid(self,value,index):

        if(index > self.size or index < 0):
            print("index Not Found")

        else:
            count_index = 0

            base_element = self.head

            next_element = base_element.next

            while next_element!=None:
                if count_index==index:
                    print("insertion between"+str(count_index)+"and"+str(count_index+1))

                    newNode=LinkedList.Node(value,next_element)
                    base_element.next=newNode
                    self.size+=1

                    break

                else:
                    base_element=next_element
                    next_element=next_element.next
                    count_index+=1

                    if (count_index==(self.size-1)):
                        self.insertLast(value)
                        break

    #Delete the elment at a specific index of the LL
    def deleteMiddle(self,index):

        if(index > self.size or index < 0):
            print("index Not Found")

        else:
            count_index = 0

            base_element = self.head

            next_element = base_element.next

            while next_element!=None:
                if count_index==index:
                    print("deletion between"+str(count_index)+"and"+str(count_index+1))

                    base_element.next=next_element.next
                    self.size-=1

                    break

                else:
                    base_element=next_element
                    next_element=next_element.next
                    count_index+=1

                    if(count_index==self.size-1):
                        self.deleteLast()

            return next_element.element
        

#Testing LL Class

testing=LinkedList(0,0)
testing.deleteMiddle(5)
testing.deleteFirst()
testing.insertFront(2)
testing.insertFront(3)
testing.insertFront(4)
testing.insertLast(5)
testing.insertLast(10)
testing.insertMid(203,2)
testing.insertMid(226,6)
# Insertion Works Like Expected
print(testing.deleteLast())
print(testing.deleteMiddle(1))
print(testing.deleteLast())
print(testing.deleteLast())
print(testing.deleteLast())
print(testing.getAll())
# Deletion Is Also Working as Expected
        







    
