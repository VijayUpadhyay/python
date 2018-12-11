#We use @func_name to specify a decorator to be applied on another function.
# Adds a welcome message to the string returned by fun(). Takes fun() as parameter and returns welcome(). 
def decorate_message(fun): 
    print("2.........")
    # Nested function 
    def addWelcome(site_name): 
        print("3.........")
        print("5......Welcome %s !!" %(fun(site_name)))
        return "Welcome " + fun(site_name) +" !!"
    # Decorator returns a function 
    print("4.........")
    return addWelcome 
@decorate_message
def site(site_name): 
    print("1.........")
    return site_name+" Upadhyay";
# Driver code 
# This call is equivalent to call to decorate_message() with function site("GeeksforGeeks") as parameter 
print(site("Vijay"))
print(decorate_message(site("Rakesh")))