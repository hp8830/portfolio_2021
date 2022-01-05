class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

stack_object = AddingStack()

for i in range(10):
    stack_object.push(i)
print(stack_object.sum())