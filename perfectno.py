num_str=input("\n\t\tNumber:")
num=int(num_str)
length=len(num_str)
print(f"Perfect Numbers from 1 to {num} are :")
for k in range(2,num+1):
    total=1
    for i in range(2,k):
        if k%i==0:
            total+=i
    if total == k:
        print("%d"%(k))
    