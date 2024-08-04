def div(a,b):
    try:
        result=a/b
    except ZeroDivisionError:
        print("Error:Division by zero is not allowed")
        result=None
    except TypeError:
        print("Error: Invalid Input Type")
        result=None
    return result
print(div(5,0))
print(div(5,"5"))
