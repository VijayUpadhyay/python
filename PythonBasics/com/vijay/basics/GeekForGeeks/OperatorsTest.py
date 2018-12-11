def cyu2(s1, s2):
    x = len(s1)
    y = len(s2)
    return x-y

z = cyu2("Yes", "no")
if z > 0:
    print("First one was longer")
else:
    print("Second one was at least as long")