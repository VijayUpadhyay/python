def outerFunction(text): 
    text = text 
    def innerFunction(): # provides output only after being called.
        print(text) 
    return innerFunction # Note we are returning function WITHOUT parenthesis
if __name__ == '__main__': 
    myFunction = outerFunction('Vijay!') 
    myFunction() 