#using for loop

A = [[1,2,3],
     [4,5,6],]
T = [[0,0],
     [0,0],
     [0,0]]
for i in range (len(A)):
    for j in range (len(A[0])):
        #print (j)
        #print (i)
        T[j][i]=A[i][j]
#print (T)
for i in T:
    print (i)