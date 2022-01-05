def powers_of_2(n):
    power = 3
    for i in range(n):
        yield power
        power *= 4


for v in powers_of_2(3):
    print(v)

