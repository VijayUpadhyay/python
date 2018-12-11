import itertools
#dropwhile vs takewhile
li = [2, 4, 6, 7, 8, 10, 20]
iti = iter(li)
#After first fail/false it will return all elements 
print ("The values after condition returns false : ",end="") 
print (list(itertools.dropwhile(lambda x : x%2==0,li))) 
# it will iterate until it fails/false
print ("The list values till 1st false value are : ",end="") 
print (list(itertools.takewhile(lambda x : x%2==0,li )))
# using tee() to make a list of iterators. Makes list of 3 iterators having same values. 
it = itertools.tee(iti, 3) 
# printing the values of iterators 
print ("The iterators are : ") 
for i in range (0,3): 
    print (list(it[i])) 