#key mapping
student={
    'name':"Harry",
    'age':22,
    'school':"DAV School"
}
student['gender']="Male"
print(f"The students name is {student['name']} and age is {student['age']}")
print(student.get("name"))
print(student.get("gender"))
print(student.get("Hollow"))
#print(student['hollow']) (ERROR)

#program to take name,age,gender of 3 students from user and print it
number=3
stu=[]
for i in range(3):
    name=input("Enter the name")
    age=int(input("Enter the age"))
    gender=input("Enter the gender")
    student= {
        "name":name,
        "age":age,
        "gender":gender
    }
    stu.append(student)
print(stu)

for student in stu:
    print(student['name'])
    print(student['age'])
    print(student['gender'])
