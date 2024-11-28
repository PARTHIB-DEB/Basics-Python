class ABC:
    def __init__(self,a,b) -> None:
        self.a,self.b=a,b
    def addTwoNum(self):
        print(f'sum of {self.a} and {self.b} is {self.a+self.b}')
class child:
    def __init__(self,a,b,c) -> None:
        self.a,self.b,self.c=a,b,c
    def addTwoNum(self):
        print(f'sum of {self.a} , {self.b} , {self.c} is {self.a+self.b+self.c}')

obj_par=ABC(10,11)
obj_par.addTwoNum()
obj_child=child(10,11,12)
obj_child.addTwoNum()
