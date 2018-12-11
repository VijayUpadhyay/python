def myFun(arg1, *argv): 
    print ("First argument :", arg1) 
    print("Length of *argv",len(argv))
    for arg in argv: 
        print("Next argument through *argv :", arg) 
myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')