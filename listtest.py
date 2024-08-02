x=[]
for i in range(0,5):
    y=input('Enter the name of student')
    x.append(y)
print("List of students",x[0:5])
for i in x:
    if (i[0]=="A" or i[0]=="a"):
        print(i)
