#a="My name is megha i am from mallapur"
#vowels = "aeiou"
#a=a.casefold()
#print (a)
#count = {}.fromkeys(vowels, 0)
#print (count)

#for char in a:
#   if char in count:
#      count[char]+=1
#print (count)


a="My name is megha i am from mallapur"
vowels = "aeiou"
a=a.casefold()

count ={key:sum([1 for char in a if char == key])for key in vowels}
print (count)