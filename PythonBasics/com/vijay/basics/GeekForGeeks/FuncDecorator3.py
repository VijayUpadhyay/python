def squareOfSum(func):
    func.data=100
    return func
@squareOfSum
def addNums(x,y):
    return x+y
print(addNums(3,4),end =" ")
print(addNums.data,end =" ")
print(squareOfSum(addNums).data,end =" ")