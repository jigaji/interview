from collections import deque

myStack = deque('abcd')

opening = tuple('({[')
closing = tuple(')}]')
match = dict(zip(opening, closing))
correct = deque()

str1 = '[[{())}]'
str2 = '[([])((([[[]]])))]{()}'


class Stack:

    def isEmpty(self, stack):
        if len(stack) == 0:
            return True
        else:
            return False

    def push(self, stack, new_element):
        stack.append(new_element)
        return stack

    def pop(self, stack):
        return stack.pop()

    def peek(self, stack):
        return stack[-1]

    def size(self, stack):
        return len(stack)

    def isMatched(self, string):

        for letter in string:
            if letter in opening:
                correct.append(match[letter])
            elif letter in closing:
                if not correct or letter != correct.pop():
                    return 'Несбалансированно'
        return 'Сбалансированно'

if __name__ == '__main__':
    print(Stack().isEmpty(myStack))
    print(Stack().isMatched(str1))