mylist=[1,2,3,'parthib','kumar',(1,2,3),5]
string="Parthib"
# print(list(enumerate(mylist)))
# print(dict(enumerate(mylist)))
# print(list(enumerate(string)))
# print(dict(enumerate(string)))

mylist1=mylist[0:3]
print(mylist1)
mylist2=tuple(mylist[4:len(mylist)])
print(mylist2)
mylist3=dict(zip(mylist1,mylist2))
print(mylist3)