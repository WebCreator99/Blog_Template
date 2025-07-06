cp={
    "Bengaluru":84,
    "Mysuru":11,
    "Hubballi":9,
    "Mangaluru":5
}
lc = {city:pop for city,pop in cp.items() if pop>10}
#lc = {key:value for key,value in cp.items() if value>10}
print(lc)