l = [1,23,43,434,32]
dl = []
#print(l)

for num in l:
    dl.append(num*2)
    print(dl)
    #print(l)


len = [7, 8, 9, 10, 11, 12, 13, 14, 15]
for num in len:
    print(num)


for i in range(1,10,3):
    print(i, end=" ")   

for i in range(1,6):
    for j in range(1,11):
        print(f"{i} X {j} = {i * j}")

    print()