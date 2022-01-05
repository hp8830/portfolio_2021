class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val


class CountingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__c=0
    # Fill the constructor with appropriate actions.
    #

    def get_counter(self):
        return self.__c
    #
    # Present the counter's current value to the world.
    #

    def pop(self):
        val= Stack.pop(self)
        self.__c+= 1
        return val
    #
    # Do pop and update the counter.
    #
	

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()
print(stk.get_counter())
