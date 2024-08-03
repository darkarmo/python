def add(*args):
    print(args)
    sum=0
    for i in args:
        sum+=i
    return sum

print(add(3,4,5,6,7,8,9,10))
def greet(firstname,lastname):
    print(f"Hello,{firstname}{lastname}")
greet("John","Doe")
greet(lastname="Doe",firstname="John")