'''
1
23
456
78910
'''

row_column=int(input("No of rows/Columns:"))
k=1
for i in range(1,row_column+1):
    for j in range(1,i+1):
        print(f"{k}",end="")
        k+=1
    print("\n")