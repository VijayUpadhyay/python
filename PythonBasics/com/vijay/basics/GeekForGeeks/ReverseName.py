nameVal="Vijay Upadhyay"
arrVal=nameVal.split(" ")
print(arrVal)
#range([start], stop[, step])
for i in range(len(arrVal),0,-1): 
    print(arrVal[i-1])
    