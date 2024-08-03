'''
count=1
while (count<=10):
    print(count)
    count=count+1
'''
#program to ask user name of student and store it in a list and ask user until to select Y or N
name=[]
n="y"
while (n=="y" or n=="Y"):#(n!="N" or n!=="n")
    stu=input("Write the name of the student")
    name.append(stu)
    n=input("Do you want to add more (Y for yes , N for no )")

print(name)