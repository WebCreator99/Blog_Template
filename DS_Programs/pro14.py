students = [
    {"name":"chandan", "marks":10},
    {"name":"kiran", "marks":100},
    {"name":"vijay", "marks":50},
]

students.sort(key= lambda x: x["marks"], reverse=True)
print(students)

#marks = [10,150,50]
#marks.sort()
#print(marks)
#marks.sort(reverse=True)
#print(marks)