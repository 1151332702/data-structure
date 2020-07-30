class Stack(object):
    def __init__(self):
        self.container = list()

    def push(self, v):
        self.container.append(v)

    def is_empty(self):
        return len(self.container) == 0

    def top(self):
        if not self.is_empty():
            return self.container[-1]
        else:
            raise Exception('container is empty')

    def pop(self):
        if not self.is_empty():
            return self.container.pop(-1)
        else:
            raise Exception('container is empty')


# 栈混洗问题
def f1(stack_src, stack_dest):
    mid_stack = Stack()
    # 对dest逆序
    tmp = Stack()
    while not stack_dest.is_empty():
        tmp.push(stack_dest.pop())
    stack_dest = tmp
    while not stack_src.is_empty():
        mid_stack.push(stack_src.pop())
        if mid_stack.top() == stack_dest.top():  # 开始一轮pop
            while not mid_stack.is_empty() and not stack_dest.is_empty() and mid_stack.top() == stack_dest.top():
                mid_stack.pop()
                stack_dest.pop()
            if mid_stack.is_empty():
                continue
            else:
                return False
    return mid_stack.is_empty()

# 优先级列表
# key 栈定运算符 value 当前运算符的dict
priority = {
    '+': {'+': '>', '-': '>', '*': '<', '/': '<', '^': '<', '!': '<', '(': '<', ')': '>', '&': '>'},
    '-': {'+': '>', '-': '>', '*': '<', '/': '<', '^': '<', '!': '<', '(': '<', ')': '>', '&': '>'},
    '*': {'+': '>', '-': '>', '*': '>', '/': '>', '^': '<', '!': '<', '(': '<', ')': '>', '&': '>'},
    '/': {'+': '>', '-': '>', '*': '<', '/': '<', '^': '<', '!': '<', '(': '<', ')': '>', '&': '>'},
    '^': {'+': '>', '-': '>', '*': '>', '/': '>', '^': '>', '!': '<', '(': '<', ')': '>', '&': '>'},
    '!': {'+': '>', '-': '>', '*': '>', '/': '>', '^': '>', '!': '>', '(': ' ', ')': '>', '&': '>'},
    '(': {'+': '<', '-': '<', '*': '<', '/': '<', '^': '<', '!': '<', '(': '<', ')': '=', '&': ' '},
    ')': {'+': ' ', '-': ' ', '*': ' ', '/': ' ', '^': ' ', '!': ' ', '(': ' ', ')': ' ', '&': ' '},
    '&': {'+': '<', '-': '<', '*': '<', '/': '<', '^': '<', '!': '<', '(': '<', ')': ' ', '&': '='},
}


# 中缀表达式  表达式求值问题
def calc_factorial(n):
    r = 1
    for i in range(1, n + 1):
        r *= i
    return r


def calc_value(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2
    elif op == '^':
        return n1 ** n2
    else:
        raise Exception('illegal operation')


def f2(expr):
    operator_stack = Stack()
    number_stack = Stack()
    operator_stack.push('&')
    pre = '&'
    for char in expr:
        if char.isdigit():
            if pre.isdigit():
                number_stack.push(number_stack.pop() * 10 + int(char))
            else:
                number_stack.push(int(char))
        else:
            while priority[operator_stack.top()][char] == '>':
                if char == '!':
                    r = calc_factorial(number_stack.pop())
                else:
                    r = calc_value(number_stack.pop(), number_stack.pop(), operator_stack.pop())
                number_stack.push(r)
            else:
                p = priority[operator_stack.top()][char]
                if p == '<':
                    operator_stack.push(char)
                elif p == '=':
                    operator_stack.pop()
                elif operator_stack == ' ':
                    raise Exception('illegal expr')
        pre = char
    return number_stack.pop()


if __name__ == '__main__':
    # # 栈混洗
    # s1 = Stack()
    # s1.push(1)
    # s1.push(2)
    # s1.push(3)
    # s2 = Stack()
    # s2.push(2)
    # s2.push(1)
    # s2.push(3)
    # print(f1(s1, s2))

    # 中缀表达式
    s = '1+2*3+4'
    print(f2(s + '&'))