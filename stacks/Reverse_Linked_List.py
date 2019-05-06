"""
This code reverses a linked list using explicit stack
"""

from data_structures.LinkedList.Linked_List import LinkedList
from data_structures.stacks.stacks import Stack


def reverse(link):
    s = Stack()

    temp = link
    while temp:
        s.push(temp)
        temp = temp.next

    while not s.is_empty():
        temp = s.pop()
        temp.next = s.top()


    link = temp


if __name__ == "__main__":

    new_link = LinkedList()
    while True:
        inp = str(input('new node: '))
        if inp == "C":
            break
        new_link.insert(inp, 1)
    print('forward: ')
    new_link.print_node()
    reverse(new_link)
    print('reverse: ')
    new_link.print_node()




