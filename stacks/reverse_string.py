"""
This code illustrates the reversal of input string using stack data structure
"""

from data_structures.stacks.stacks import Stack


def reverse(string):

    s = Stack()

    for st in string:
        s.push(st)

    while not s.is_empty():
        print(s.top())
        s.pop()


if __name__ == "__main__":

    st = str(input('String: '))
    print('reverse: ')
    reverse(st)
