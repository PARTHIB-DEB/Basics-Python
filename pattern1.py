'''
*
**
***
****
'''

row_column=int(input("No of rows/Columns:"))
for i in range(1,row_column+1):
    for j in range(1,i+1):
        print("*",end="")
    print("\n")