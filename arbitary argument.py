def add(*args):
    print(args)
    sum=0
    for i in args:
        sum+=i
    return sum

print(add(3,4,5,6,7,8,9,10))
#default values
def greet(firstname,lastname):
    print(f"Hello,{firstname}{lastname}")
greet("John","Doe")
greet(lastname="Doe",firstname="John")

def display_person(firstname=None,middlename=None,lastname=None):
    if middlename==None:
        print(f"{firstname} {lastname}!")
    else:
        print(f"{firstname} {middlename} {lastname}!")
display_person(firstname="John",lastname="Doe")
