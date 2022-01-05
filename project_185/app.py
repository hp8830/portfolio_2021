#List comprehensions
#May also be used within list comprehensions 

def powers_of_2(n):
    power = 2
    for i in range(n):
        yield power
        power *= 3


t = [x for x in powers_of_2(3)]
print(t)