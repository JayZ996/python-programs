def Fib(n):
    if n<=0:
        print("Enter a positive number")

    elif n==1 or n==2:
        return 1

    else:
        return Fib(n-1) + Fib(n-2)

user = int(input("Enter the nth term: "))
print(Fib(user-1), "is the nth term")