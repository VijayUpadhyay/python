import itertools  
li = [2, 4, 5, 7, 8, 10, 20] 
li1 = [ (1, 10, 5), (8, 4, 1), (5, 4, 9), (11, 10 , 1) ]
# using islice() to slice the list acc. to need starts printing from 2nd index till 6th skipping 2 
print ("The sliced list values are : ", end="") 
print (list(itertools.islice(li, 1, 6, 2))) 
# using starmap() for selection value acc. to function selects min of all tuple values 
print ("The values acc. to functions(min/max) are : ") 
print ("min among tuples: ",list(itertools.starmap(min, li1))) 
print ("max among tuples: ",list(itertools.starmap(max, li1))) 
