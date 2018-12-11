import itertools
list1=[1,15,12,88]
list2=[4,5,66,99]
print("product: ",list(itertools.product(list1,list2)))
print("permutations: ",list(itertools.permutations(list1,3)))
print("combinations: ",list(itertools.combinations(list1,3)))
print("combinations: ",list(itertools.combinations_with_replacement(list1,3)))