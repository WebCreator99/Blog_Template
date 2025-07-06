students =["Kumar","Anand", "Geetha"]
students.sort()

marks = [85, 90, 78]
marks.sort()

student_marks={}

for index, student in enumerate(students):
    student_marks[student] = marks[index]

print(student_marks)





Education =["LKG","UKG","Primery","HighSchool","PUC", "Degree"]
price=[500,600,100,200,300,800]

Details={}

for index, studyWay in enumerate(Education):
    Details[studyWay] = price[index]

print(Details)