'''
    1
   23
  345
 4567
'''

row_column=int(input("No of rows/Columns:"))
for i in range(1,row_column+1):
    for j in range(1,row_column-i+1):
        print("\t",end="")
    for k in range(i,2*i):
        print(k,end="\t")
    print()
    
'''
        1
      2 3
    3 4 5
  4 5 6 7
'''
# limit=int(input("Row/Col:"))
# for i in range(1,limit+1):
#     for k in range(1,limit-i+1):
#         print(" ",end="")
#     for j in range(i,2*i):
#         print(j,end="")
#     print()