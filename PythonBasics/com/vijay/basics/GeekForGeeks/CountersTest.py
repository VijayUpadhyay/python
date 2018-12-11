from collections import Counter
# With sequence of items  
print (Counter(['B', 'B', 'A', 'B', 'C', 'A', 'B', 'B', 'A', 'C', 'A', 'C'])) 
# with dictionary 
print (Counter({'A':3, 'B':5, 'C':2})) 
# with keyword arguments 
print (Counter(A=3, B=5, C=2)) 
demoCounter = Counter()
demoCounter.update([44, 4, 6, 'rth', 88, 99])
print(demoCounter)
demoCounter.update([88, 99, 44, 4, 6])
print(demoCounter)
for i in demoCounter:
    if demoCounter[i] == 1:
        print("%s is unique" % (i))
