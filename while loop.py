'''
count=1
while (count<=10):
    print(count)
    count=count+1
'''
#program to ask user name of student and store it in a list and ask user until to select Y or N
name=[]
n="y"
#while (n=="y" or n=="Y"):#
'''while(n!="N"):
    stu=input("Write the name of the student")
    name.append(stu)
    n=input("Do you want to add more (Y for yes , N for no )")

print(name)
'''
stu="Dummy"
#until last character in A or a
while(stu[-1]!="a"):
    stu=input("Write the name of the student")
    name.append(stu)

print(name)