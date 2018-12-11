from _functools import partial
def tesfFunc(a, b, c, d):
    print("Val a: %d, b: %d, c: %d, d: %d" %(a,b,c,d))
    d = a * a + b
    return d + c
val_a = partial(tesfFunc, c=2, d=6, b=7)
print(val_a(3))
val_b = partial(tesfFunc, a=2,d=4, b=17)
print(val_b(3))