from functools import partial
# A normal function 
def add(a, b, c): 
    return 100 * a + 10 * b + c 


# A partial function with b = 5 and c = 2 
add_part = partial(add, c=2, b=5) 
# Calling partial function 
print(add_part(3)) 
