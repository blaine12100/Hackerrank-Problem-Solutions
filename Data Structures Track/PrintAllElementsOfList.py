'''
Print All the elements of the Linked List.The process involves visitng
all the elements of the list sequentially while the current element is not none
If not,then print the value fo the element and assign the new element to the next of the
previous element 
'''


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

# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def printLinkedList(head):
    if head.data == None:
        z = 0

    else:
        base_element = head

        while base_element != None:
            print(base_element.data, sep="\n")
            base_element = base_element.next


if __name__ == '__main__':
    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    printLinkedList(llist.head)
