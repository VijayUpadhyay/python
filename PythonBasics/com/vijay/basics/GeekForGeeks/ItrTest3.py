import itertools
from collections import Counter
list1 = [1, 2, 3, 4, 5, 6, 44]
list2 = [44, 55, 77, 55, 68, 88]
list3 = [44, 77, 854, 545, 8, 89]
print("Summation of 1st list: ", list(itertools.accumulate(list1)))
print("Summation of 2nd list: ", list(itertools.accumulate(list2)))
print("Summation of 3rd list: ", list(itertools.accumulate(list3)))
print("Chain of lists is: ", list(itertools.chain(list1, list2, list3)))
finalList = list(itertools.chain(list1, list2, list3))
print("finalList after counter impl: ", Counter(finalList))
