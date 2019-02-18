'''Comparing 2 Linked Lists.For this we need to iterate over both the lists until either of them
is none.And we need to keep incementing the size at each pass.If either of the lists is becomes none
we switch the flag to false indicating the lengths are not the same and we return the value
accordingly'''

#!/bin/python3

import os
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

# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def compare_lists(llist1, llist2):
    base1 = llist1
    base2 = llist2

    size1 = 0
    size2 = 0

    # All elements are equal
    list_node_flag = True

    while base1 != None or base2 != None:
        if base1 == None and base2 != None:
            list_node_flag = False
            break
        elif base2 == None and base1 != None:
            list_node_flag = False
            break

        if base1.data != base2.data:
            list_node_flag = False
            break

        else:
            size1 += 1
            size2 += 1

            base1 = base1.next
            base2 = base2.next
    # print(list_node_flag,size1,size2)

    if list_node_flag and (size1 == size2):
        return 1
    else:
        return 0


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist1_count = int(input())

        llist1 = SinglyLinkedList()

        for _ in range(llist1_count):
            llist1_item = int(input())
            llist1.insert_node(llist1_item)

        llist2_count = int(input())

        llist2 = SinglyLinkedList()

        for _ in range(llist2_count):
            llist2_item = int(input())
            llist2.insert_node(llist2_item)

        result = compare_lists(llist1.head, llist2.head)

        fptr.write(str(int(result)) + '\n')

    fptr.close()
