l = [x for x in range(1, 11)]
print(l)

edl = [x**2 for x in l if x%2==0]
#[exp for item in collection if condition]
#even numbers square

print(edl)