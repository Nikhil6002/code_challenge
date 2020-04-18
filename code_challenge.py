def calc(a,b,op):
    if(op=="add"):
        return (a+b)
    elif(op=="subtract"):
        return (a-b)
    else:
       return "Invalid operation"

a=int(input("Enter 1st number: "))
b=int(input("Enter 2nd number: "))
op=input("Enter the operation 'add' or 'subtract': ")

result=calc(a,b,op)
print(result)
