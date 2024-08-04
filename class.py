class student():
    name="Hyu"
    age="22"
    def __init__(self,name=None,age=None): #constructor
        print(f"I am called {self.name}")
        self.name=name
        self.age=age
    def intro(self):
        print(f"My name is {self.name} and I am {self.age} year old.")

stu=student("Harry",23)
stu1=student("Karin",45)
print(type(stu))

print(stu.name)
print(stu.age)
print(stu1.name)
print(stu1.age)
stu.intro()
stu1.intro()
stu2=student()

stu2.name="Ramesh"
stu2.age=23
stu2.intro()
