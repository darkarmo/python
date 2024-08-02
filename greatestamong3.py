#int(a),int(b),int(c)=input("Enter 3 numbers").split()
a=int(input("Enter 1st number"))
b=int(input("Enter 2nd number"))
c=int(input("Enter 3rd number"))
if(a>b and a>c):
    print("The greatest is",a)
elif(b>a and b>c):
    print("The greatest is ",b)
else:
    print("The greatest is ",c)

