def sortWithVal(val):
    byteval = val.bytes()
    return int(byteval)


list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [331, 22, 3, 34, 5 , -100];
list3 = ["a", "b", "c", "d"];
print(list1.count(1997))
print(list3.sort(reverse=True))
print(list3)
print("list1[-3]: ", list1[-3])  # length minus negative index
print(min(list2))
print(max(list2))
list1.append("newElement")
print(list1)
list1.append(list2)  # will add as single element
print(list1)
list1.extend(list2)  # will add every element of list2 into list1 as single element
print(list1)
