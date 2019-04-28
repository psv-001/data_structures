'''
This code illustrated wotking implementation of
Linked list and operations of linked list
'''


class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, data, pos):
        """
        This method inserts new node at given position
        :param data:
        :param pos:
        :return:
        """
        node = Node(data)
        if pos == 1:
            node.next = self.head
            self.head = node
            return
        temp = self.head
        for i in range(1, pos-1):
            temp = temp.next
        node.next = temp.next
        temp.next = node

    def delete(self, pos):
        """
        This method deletes the node at given position
        :param pos:
        :return:
        """
        temp = self.head
        if pos is 1:
            self.head = temp.next
            del temp
            return

        for i in range(1, pos-1):
            temp = temp.next
        temp2 = temp.next
        temp.next = temp2.next
        del temp2

    def print_node(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next


if __name__ == "__main__":
    myll = LinkedList()
    myll.insert(3, 1)  # List: 3
    myll.insert(4, 2)  # List: 3,4
    myll.insert(5, 3)  # List: 3,4,5
    myll.print_node()
    myll.delete(2)
    print("After delete")
    myll.print_node()  # List: 3,5
    myll.insert(1, 1)  # List: 1,3,5
    print('----------')
    myll.print_node()
    myll.delete(1)  # List: 3,5
    print('----------')
    myll.print_node()

