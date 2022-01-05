def fun(n):
    for i in range(n):
        yield i

        #yield instead of return turns teh function into a generator 