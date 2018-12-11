def myFun(arg1, arg2, arg3): 
    print("arg1:%s arg2:%s args:%s" %(arg1,arg2,arg3)) 
# Now we can use *args or **kwargs to pass arguments to this function :  
args = ("vibha", "rakesh", "ram") 
myFun(*args) 
kwargs = {"arg1" : "vijay", "arg2" : "madhu", "arg3" : "rakesh"} 
myFun(**kwargs)