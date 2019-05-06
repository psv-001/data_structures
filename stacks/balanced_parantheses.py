"""
This code illustrates the compilation process for balanced parenthesis using stack.
"""
from data_structures.stacks.stacks import Stack


def check_parenthesis(parenthesis):

    st = Stack()

    close_open = {")": "(", "]": "[", "}": "{"}

    if parenthesis[0] in close_open.keys():
        return "unbalanced parenthesis"

    for par in parenthesis:
        if par in close_open.values():
            st.push(par)
        elif par in close_open.keys():
            if st.top() == close_open[par]:
                st.pop()
            else:
                return "unbalanced parenthesis"
    if st.is_empty():
        return "Success: Parenthesis are balanced"
    return "unbalanced parenthesis"


if __name__ == "__main__":
    par = str(input("Enter Parenthesis: "))
    print(check_parenthesis(par))
