"""
This code illustrates the functioning of postfix, prefix and infix operations using stack data structures
"""
from data_structures.stacks.stacks import Stack

calc = {'+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y}

operators = ['*', '/', '+', '-']


def evaluate_postfix(expr):
    st = Stack()

    for op in expr:
        if op not in calc.keys():
            st.push(op)
        else:
            op1 = int(st.pop())
            op2 = int(st.pop())
            res = calc[op](op1, op2)
            st.push(res)

    result = st.pop()

    return result


def evaluate_prefix(expr):
    st = Stack()
    for ind in range(-1, - (len(expr) + 1), -1):
        if expr[ind] not in calc.keys():
            st.push(expr[ind])
            st.top()
        else:
            op1 = int(st.pop())
            op2 = int(st.pop())
            res = calc[expr[ind]](op2, op1)
            st.push(res)

    result = st.pop()

    return result


def infix_to_postfix(exp):
    st = Stack()
    post = ""

    def _isOpeningBracket(ex):
        return ex in ('(', '{', '[')

    def _isclosingBracket(ex):
        return ex in (')', "}", ']')

    def _isHigherPrecedence(ex1, ex2):
        return operators.index(ex1) > operators.index(ex2)
    #import pdb; pdb.set_trace()
    for e in exp:
        if _isOpeningBracket(e):
            st.push(e)
        elif e in operators:
            st.push(e)
        elif e in operators and not _isHigherPrecedence(e, st.top()):
            while not st.is_empty():
                op = st.pop()
                post += op
        elif _isclosingBracket(e):
            while not _isOpeningBracket(st.top()):
                op = st.pop()
                post += op
            st.pop()
        else:
            post += e
    while not st.is_empty():
        op = st.pop()
        post += op

    return post


if __name__ == "__main__":
    infix_exp = str(input('enter infix expression to convert to postfix: '))
    pre_exp = str(input('enter prefix expression: '))
    post_exp = str(input('enter postfix expression: '))

    print('Infix to Postfix : ', infix_to_postfix(infix_exp))
    print('Evaluating prefix: ', evaluate_prefix(pre_exp))
    print('Evaluating Postfix: ', evaluate_postfix(post_exp))
