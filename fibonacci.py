n=int(input("enter length of series:"))
a=int(input("enter first digit:"))
b=int(input("enter second digit:"))
for i in range(n-2):
    fib1=a+b
    a=b
    b=fib1
    fib1=a+b
    print("",fib1)
 
