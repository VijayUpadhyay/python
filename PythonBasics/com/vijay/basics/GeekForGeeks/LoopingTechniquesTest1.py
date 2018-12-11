list1 = [111, 22, 33, 54, 22, 11, 44, 33, 55, 11, 19]
for key, val in enumerate(list1):
    print(key, ":", val, end=" * ")
questions = ['name', 'colour', 'shape'] 
answers = ['apple', 'red', 'a circle']
print()
for que, ans in zip(questions, answers):
    print("Que is: %s and its Ans is: %s" % (que, ans))
d = { "geeks" : "for", "only" : "geeks" } 
# for key1, val1 in d.iteritems():
for key1, val1 in d.items():
    print(key1, val1, end=" ** ")
print()
for item in sorted(list1):
    print(item, end=" ")
print()
for item in set(list1):
    print(item, end=" ")
print()
for item in sorted(set(list1)):
    print(item, end=" ")
print()
for i in reversed(list1):
    print(i, end=" * ")
print()
for i in reversed(range(1, 10, 3)): 
    print (i,end=" ")