def primefactors(num):
    mylist = []
    for i in range(2, num):
        if num % i == 0:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                mylist.append(i)
        else:
            continue
    else:
        return mylist
num = int(input("Enter Number:"))
print(f"Prime factors of {num} are : {primefactors(num)}")
