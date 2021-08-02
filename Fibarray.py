FibArr = [0,1]

def fibonacci(n):

    if n<=0:
        print("Incorrect input")

    elif n<=len(FibArr):
        return FibArr[n-1]

    else:
        temp = fibonacci(n-1) + fibonacci(n-2)
        FibArr.append(temp)
        return temp
user = int(input("Enter nth term"))
print(fibonacci(user))
print(FibArr)