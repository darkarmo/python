a=int(input("Enter first number"))
b=int(input("Enter second number"))
n=input("Enter the operator")

def add(a,b):
    sum=a+b
    return sum
def sub(a,b):
    subtract=a-b
    return subtract
def mul(a,b):
    multiply=a*b
    return multiply
def div(a,b):
    division=a/b
    return division
if(n=="+"):
    print(add(a,b))
elif(n=="-"):
    print(sub(a,b))
elif(n=="*"):
    print(mul(a,b))
elif(n=="/"):
    print(div(a,b))
else:
    print("Invalid Operator")
