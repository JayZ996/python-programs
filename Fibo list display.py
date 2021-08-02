N = int(input("Enter the no of terms"))

# first two terms
n1, n2 = 0, 1
count = 0
arr = []
# check if
if N<0:
    print("Enter a positive number")

elif N ==0:
    arr.append(0)

elif N == 1:
    print("Fibonacci series upto", N)
    arr.append(n1)

else:
    print("Fibonacci series upto", N)
    while(count<N):
        arr.append(n1)
        nth = n1+n2
        #update values
        n1=n2
        n2 = nth
        count += 1
print(arr)



