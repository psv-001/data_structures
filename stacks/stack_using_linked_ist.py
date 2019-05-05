"""
This code illustrates the implementation of stack data structure
using Singly Linked list data structure.
"""


class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:

    def __init__(self):
        self.head = None

    def push(self, data):

        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        newNode.next = self.head
        self.head = newNode

    def pop(self):

        temp = self.head
        if self.head is None:
            return "stack is empty"
        self.head = temp.next
        del temp

    def is_empty(self):
        return self.head is None

    def top(self):
        return self.head.data


if __name__ == "__main__":
    s = Stack()
    s.push(1)              # s = 1
    print(s.top())         # 1
    s.push(2)              # s = 2, 1
    print(s.top())         # 2
    s.push(3)              # s = 3, 2, 1
    print(s.top())         # 3
    s.pop()
    print(s.top())         # 2
    print(s.is_empty())    # false
    s.pop()
    print(s.top())         # 1
    s.pop()
    print(s.is_empty())    # true
