num_str=input("\n\n\t\tNumber:")
num=int(num_str)
length=len(num_str)
total=0
while(num>0):
    rem=num%10
    total=(total*10)+rem
    num=num/10
if total == int(num_str):
    print(f"{num_str} is a Palindrome number")
else:
    print(f"{num_str} is NOT a Palindrome number")