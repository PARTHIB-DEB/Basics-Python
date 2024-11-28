n,k=map(int,input().split(" "))
n_list = [int(i) for i in str(n)]
while(k>0):
    if n_list[len(n_list)-1]==0:
        n_list.pop()
    else:
        n_list[len(n_list)-1] -= 1
    k-=1
num=0        
for i in range(len(n_list)):
    num+=(10**(len(n_list)-i-1)*n_list[i])
print(num)