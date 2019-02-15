'''Insert Node at a specific index in the Linked List.For this,we have
to maintain 2 pointers,one for the previous element and the second one
for the next element and an index.We have to Manually count the element 
which we visit and if it is equal to our index then we change the reference
of the next and the previous elements.And we point our new created node to the 
next of the element which the previous node was poinint to earlier.'''

#!/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def insertNodeAtPosition(head, data, position):

    if head == None:
        newNode = SinglyLinkedListNode(data)
        newNode.next = None
        head = newNode

    else:
        base_count = 1
        base_element = head
        next_element = base_element.next

        while base_element != None:
            # print(base_element.data)
            if base_count == position:
                newNode = SinglyLinkedListNode(data)
                base_element.next = newNode
                newNode.next = next_element
                break

            else:
                base_element = next_element
                next_element = next_element.next
                base_count += 1

    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insertNodeAtPosition(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ', fptr)
    fptr.write('\n')

    fptr.close()
