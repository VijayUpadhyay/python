from _functools import partial
def tesfFunc(a, b=2, c=3, d=4):
    print("Val a: %d, b: %d, c: %d, d: %d" %(a,b,c,d))
    d = a * a + b
    return d + c
varVal=partial(tesfFunc)
print(tesfFunc(3))