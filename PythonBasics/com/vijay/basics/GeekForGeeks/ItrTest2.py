class Test(object):

    # # Constructor. __init__ will have double underscore.
    def __init__(self, val):
        self.val = val

    # Called when iteration is initialized 
    def __iter__(self):
        self.x = 10
        return self

    # To move to next element
    def __next__(self):
        # Stores current value of x .
        x = self.x
        # Stop iteration if limit is reached 
        if x > self.val:
            raise StopIteration
        # Else increment and return old value 
        self.x = x + 1
        return x

    
for i in Test(15):
    print(i, end=" ")
# raise stop iteration signal.
for i in Test(5):
    print(i, end=" ")