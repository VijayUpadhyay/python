def f():  
    s = "Me too."
    print(s) 
  
    # This program will NOT show error 
    # if we comment below line.  
    s = "Me..."
  
    print(s) 
  
# Global scope 
s = "I love Geeksforgeeks" 
f() 
print(s) 