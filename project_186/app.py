#The list() function can transform a series of subsequent generator invocations into a real list: 
def powers_of_2(n):
    power = 8
    for i in range(n):
        yield power
        power *= 2


t = list(powers_of_2(3))
print(t)

