"""
This Code illustrates the example of reversing the given Linked List
using iterative method
"""

from data_structures.LinkedList.Linked_List import LinkedList


def reverse():
    ll = LinkedList()
    current = ll.head
    prev = None
    # temp = current.next
    while current.next != None:
        next = current.next
        current.next = prev
        prev = current
        current = next


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
    print('reversing')
    reverse()
    myll.print_node()
