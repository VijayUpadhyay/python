m = [[1, 2], [3, 4], [5, 6]] 
for row in m : 
    print(row)
rez = [[m[j][i] for j in range(len(m))] for i in range(len(m[0]))]
print()
for row in rez:
    print(row) 
    
print("======================")
matrix=[(1,2,3),(4,5,6),(7,8,9),(10,11,12)] 
for row1 in matrix: 
    print(row1) 
print("\n") 
t_matrix = zip(*matrix) 
for row1 in t_matrix: 
    print(row1) 