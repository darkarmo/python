'''x=[]
for i in range(0,5):
    y=input('Enter the name of student')
    x.append(y)
print("List of students",x[0:5])
for i in x:
    if (i[0]=="A" or i[0]=="a"):
        print(i)
'''
'''
#inserting
y=[1,2,3]
index=int(input("Enter index"))
data=input("Enter data")
y.insert(index,data)
print(y)
'''
#remove
y=[1,"hari",3]
data=int(input("Enter data"))
y.remove(data)
print(y)
