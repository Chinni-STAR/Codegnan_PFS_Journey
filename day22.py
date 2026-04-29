'''
Introduction to OOP's
classes
objects
attributes
methods

OOP's:
--> object oriented language(oop) is style of programming where we model real-world things as object that
contain both data and functios(behavioural)
-->it is reusable of code and also scalability
-->

Class
-----
-->class is blueprint or template that defines what kind of data and behavior or a certain type of object
will have
syntax:
class class_name:

e.g..
class car:
    pass

object:
------
-->Instance of class i.e..represents of the class or An object is a real instance created from a class .
it is the actual thing that exists in memory while the program run
e.g..
class car:
   pass 
car1=car() #object of class
car2=car() #object of class

Attributes:
----------
-->these are variables that store data related to a class or object
'''
'''
class car:
    def __init__(self,brand,color):
        self.brd=brand
        self.color=color
car_1=car("toyota","White")
car_2=car("Audi","navy blue")
car_3=car("Thar","Red")
print(car_1.brd,car_2.color)
'''
class Car:
    def __init__(self,name,year,color):
        self.name=name
        self.color=color
        self.year=year
    def info(self):
        return f"{self.name},{self.color},{self.year}"
car1=Car("Audi","white","2012")
car2=Car("BMW","black","2010")
print(car1.info())




















