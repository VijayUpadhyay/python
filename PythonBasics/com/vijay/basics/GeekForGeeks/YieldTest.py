def printSquare():
    num=1
    while True:
        yield num*num
        num+=1
print(printSquare())
for i in printSquare():
    #check over infinite loop
    if i>100:
        break
    print(i,end=" ")