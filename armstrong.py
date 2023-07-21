num_str=input("\n\n\t\tNumber:")
num=int(num_str)
length=len(num_str)
total=0
for i in range(1,length+1):
    total+=((num%10)**length)
    num//=10