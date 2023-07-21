'''
Create an abstract class called Vehicle with the following attributes
make: a string indicating the make of the vehicle
model: a string indicating the model of the vehicle
year: an integer indicating the year the vehicle was made
color: a string indicating the color of the vehicle
Include the following methods in the class:
start(): a method that prints a message indicating the vehicle has started
stop(): a method that prints a message indicating the vehicle has stopped
drive(): an abstract method that prints a message indicating the vehicle is being driven
Create two subclasses of Vehicle called Car and Motorcycle. 
Each subclass should implement the drive() method with behavior specific to that type of vehicle.
Create an object of each subclass and call their methods to see their behavior.
'''

from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,make,model,year,color):
        self.make=make
        self.model=model
        self.year=year
        self.color=color
    
    def display(self):
        print(f"The vehicle is made by {self.make}")
        print(f"The vehicle is of type {self.model}")
        print(f"The vehicle is made in {self.year}")
        print(f"The vehicle's color is {self.color}")
    
    def start(self):
        print("The car has started")
    
    def stop(self):
        print("The car has stopped")
    
    @abstractmethod
    def drive():
        pass

class car(Vehicle):
    def __init__(self, make, model, year, color,name):
        super().__init__(make, model, year, color)
        self.name=name
    
    def drive(self):
        print(f"The car named {self.name} has 4 wheels")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, color,name):
        super().__init__(make, model, year, color)
        self.name=name
    
    def drive(self):
        print(f"The Motorcycle named {self.name} has 2 wheels")


dezire=car("Maruti","A",2018,"Steel","DEZIRE")
dezire.display()
dezire.start()
dezire.drive()
dezire.stop()