def myFun(**kwargs):
    print("Length of *kwargv:",len(kwargs))
    for key, value in kwargs.items(): 
        print ("%s == %s" %(key, value)) 
myFun(first ='Geeks', mid ='for', last='Geeks')