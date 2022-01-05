#List comprehension 
#conditional expression- a way of selecting one of two different values based on the result of a boolean expression 

the_list = []

for x in range(10):
    the_list.append(1 if x % 2 == 0 else 0)

print(the_list)