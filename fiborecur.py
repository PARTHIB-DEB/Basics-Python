def recur_fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return (recur_fibonacci(n-1)+recur_fibonacci(n-2))
limit=eval(input("How many Numbers :"))
for i in range(1,limit+1):
    print(recur_fibonacci(i))
