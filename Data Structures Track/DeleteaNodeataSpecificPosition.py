'''Delete a Position at a specific position of a list.Can also do recursively which
might be more elegant to write(Lesser lines of code),but might be difficult to understand
The Logic is very simillar to the case where we insert a node at a speciifc position of the list
You can refer this repo to get how to insert a node at a speciifc position'''
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
# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def deleteNode(head, position):

    if position == 0:
        return head.next

    else:

        base_element = head
        next_element = base_element.next

        base_count = 1

        while next_element != None:
            if base_count == position:
                base_element.next = next_element.next
                next_element = None

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

    position = int(input())

    llist1 = deleteNode(llist.head, position)

    print_singly_linked_list(llist1, ' ', fptr)
    fptr.write('\n')

    fptr.close()

