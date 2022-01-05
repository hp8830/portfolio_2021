#Practice iterators 
'''An iterator must provide two methods: __iter__() which should return the object itself and which is invoked once(needed for Py to successfully start the iteration

__next__() which is intended to return the next value (first, second and so on) of the desired series - it will be invoked by teh for/in statements in order to passs through the next iteration; if there are no more values to provide, the method should raise the StopIteration exception 
'''
class Fib:
    '''built a class able to iterate the first n values- where n is a constructor parameter of the Fibonacci numbers'''
    def __init__(self, nn):
        print("__init__")
        self.__n = nn# to store the series limit
        self.__i = 0# to track the current Fibonacci number to provide p1 and p2
        self.__p1 = self.__p2 = 1# to save the previous numbers

    def __iter__(self):
        print("__iter__")#return the iterator object iteself- extract the iterator and entrust it with teh execution of the iteration protocol 
        return self

    def __next__(self):
        print("__next__")		#creating the sequence
        '''first a print message- then updates the number of desired values, if it reaches the end of the sequence'''		
        self.__i += 1
        if self.__i > self.__n:
            raise StopIteration
        if self.__i in [1, 2]:
            return 1
        ret = self.__p1 + self.__p2
        self.__p1, self.__p2 = self.__p2, ret
        return ret


for i in Fib(10):
    print(i)#makes use of the iterator 
    '''Let us remind you - the Fibonacci numbers (Fibi) are defined as follows:

Fib1 = 1
Fib2 = 1
Fibi = Fibi-1 + Fibi-2

In other words:

the first two Fibonacci numbers are equal to 1;
any other Fibonacci number is the sum of the two previous ones (e.g., Fib3 = 2, Fib4 = 3, Fib5 = 5, and so on)'''