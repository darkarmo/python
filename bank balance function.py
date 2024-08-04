balance=10000
def Debit(n):
    global balance
    balance=balance-n
def Credit(n):
    global balance
    balance=balance+no
while(demo!="No")
    inp=int(input("What would you like to do \n"
                "1.Debit\n"
                "2.Credit\n"
                "3.Show Current balance\n"))
    num=int(input("Enter the amount"))
    if (inp==1):
            Credit(num)
            print(balance)
    elif(inp==2):
            Debit(num)
            print(balance)
    elif(inp==3):
            print(balance)
    else:
            print("INVALID")
    demo = input("Do you want to add more (Y for yes , N for no )")