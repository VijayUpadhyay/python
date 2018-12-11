from operator import __add__, __iadd__
import operator
# Immutable objects
a = 10;b = 20;m = 30;n = 40
p = operator.add(a, b)
q = operator.iadd(m, n)
print(p)
print(q)
sumVal = __add__(a, b)
print("Val for a:%d, b:%d is sum:%d" % (a, b, sumVal))
sumVal2 = __iadd__(a, b)
print("Val for a:%d, b:%d is sum:%d" % (a, b, sumVal2))
# Mutable Objects ==> updation and assignment both are carried out in case of mutable targets.
listEx = [1, 2, 3, 4]
z = operator.add(listEx, [55, 44, 99])
print("Updated list is: ", z)
print("Previously it was: ", listEx)
z2 = operator.iadd(listEx, [55, 88, 99])
print("Updated list is: ", z2)
print("Previously it was: ", listEx)  # works like a+=b principal for mutable objects.
