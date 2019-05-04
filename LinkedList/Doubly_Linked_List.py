"""
This code implements the doubly linked list.
"""


class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def insert_at_tail(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = newNode
        newNode.prev = temp

    def print_forward(self):
        print('Forward: ')
        temp = self.head
        while temp.next is not None:
            print(temp.data)
            temp = temp.next
        print(temp.data)

    def print_reverse(self):
        print('Reverse: ')
        temp = self.head
        while temp.next is not None:
            temp = temp.next

        while temp.prev is not None:
            print(temp.data)
            temp = temp.prev
        print(temp.data)


if __name__ == "__main__":
    mydll = DoublyLinkedList()
    mydll.insert_at_head(2)  # 2
    mydll.insert_at_head(4)  # 4, 2
    mydll.insert_at_head(6)  # 6, 4, 2
    mydll.insert_at_tail(1)  # 6, 4, 2, 1
    mydll.print_forward()  # 6, 4, 2, 1
    mydll.print_reverse()  # 1, 2, 4, 6

