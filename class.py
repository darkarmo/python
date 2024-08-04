class student():
    name="Hyu"
    age="22"
    def __init__(self,name,age):
        print(f"I am called {self.name}")
        self.name=name
        self.age=age

stu=student("Harry",23)
stu1=student("Karin",45)
print(type(stu))
print(stu.name)
print(stu.age)
print(stu1.name)
print(stu1.age)
