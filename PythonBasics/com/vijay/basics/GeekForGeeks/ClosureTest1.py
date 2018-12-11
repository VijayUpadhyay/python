#As we can see innerFunction() can easily be accessed inside the outerFunction body 
#but not outside of it’s body. Hence, here, innerFunction() is treated as nested 
#Function which uses text as non-local variable.
def outerFunction(text): 
    custName = text 
    def innerFunction(): 
        print(custName) 
    innerFunction() 
if __name__ == '__main__': 
    outerFunction('Ram!') 