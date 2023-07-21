'''
1.Create a class called Book with the following attributes:
title: a string representing the title of the book
author: a string representing the author of the book
genre: a string representing the genre of the book
price: a float representing the price of the book
quantity: an integer representing the quantity of the book
Provide methods to add and remove books from the book inventory. 
Ensure that the quantity is not negative after any operation. 
Implement a method to display all the books in the inventory.
'''
class Bookproto:
    books=dict()
    total=0
    def __init__(self,title,author,genre,price,quantity):
        self.title=title
        self.author=author
        self.genre=genre
        self.price=price
        self.quantity=quantity
    
    
    def add_books(self,book_no,book_name):
        my_dict=Bookproto.books
        self.book_no=book_no
        self.book_name=book_name
        my_dict[self.book_no]=book_name
        print(f"Book No : {self.book_no} and name : {self.book_name} is added!!")
        Bookproto.total+=1
    
    def remove_books(self,book_no):
        self.book_no=book_no
        if (Bookproto.total-1)>0:
            print(f"Book of No: {self.book_no} and name :{Bookproto.books[self.book_no]} is deleted")
            del Bookproto.books[self.book_no]
            Bookproto.total-=1
        else:
            print("No other Books Can be deleted")
    
    def display_books(self):
        print(f"There are Total {Bookproto.total} books")
        new_dict=Bookproto.books
        print(new_dict)
            
            

obj=Bookproto("ABCD","Eugine gold","kids",45,4)
obj.add_books(1,"Dinosours")
obj.add_books(2,"Tom and jerry")
obj.add_books(3,"Batul di great")
obj.display_books()
obj.remove_books(2)
obj.display_books()
        
            
            
            
        
            
            
        
    
    