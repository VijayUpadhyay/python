t1 = ('maths', [1, 2, 3])
print(t1)
# t[2]='mathematics' ==> TypeError: 'tuple' object does not support item assignment
t2 = ('raj', 781, 22, 111, 'user')
t3 = t1 + t2
print(t3)
list1 = [10, 11, 2, 22]
t4 = t1 + tuple(list1)
print(id(t4))
list1[2] = 788
print("After changing:")
t4 = t1 + tuple(list1)
print(id(t4))
print(t4)
