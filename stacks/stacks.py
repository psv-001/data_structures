"""
This code illustrates implimentation of stack data structure using list
and basic operations of stack
"""


class Stack:

    def __init__(self):
        self.stack = list()

    def push(self, data):
        self.stack.insert(0, data)

    def pop(self):
        return self.stack.pop(0)

    def is_empty(self):
        return self.stack == []

    def top(self):
        return self.stack[0]

    def print_stack(self):
        for i in self.stack:
            print(i)


if __name__ == "__main__":

    s = Stack()
    s.push(1)  # s = 1
    s.push(2)  # s = 2, 1
    s.push(3)  # s = 3, 2, 1
    print('-------')
    s.print_stack()
    print('-------')
    s.pop()
    s.print_stack()  # s = 2, 1
    print('-------')
    print(s.top())   # 2
    print(s.is_empty())  # False
    s.pop()   # s = 1
    s.pop()   # s = []
    print(s.is_empty())  # True
