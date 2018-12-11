my_generator = (letter for letter in 'Hello World') # creates generator object
next(my_generator) #allowed in Python 2 and Python 3
print("Done")
my_generator.next() #allowed in Python 2. raises AttributeError in Python 3