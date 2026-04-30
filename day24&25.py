
#Encapsulation
'''
-->The principle of bunding data(Attributes) and methods that operate on that data into a single unit,
which is a class

class BankAc:
    def __init__(self,balance):
        self.__balance = balance
        
    def deposite(self,amount):
        self.__balance+=amount

        
    def get_balance(self):
        return self.__balance
    
acc=BankAc(23000)
acc.deposite(7000)
print(acc.get_balance())
'''

#Inheritance
'''
-->acquiring properties from parent class(Base class) to child class(subclass)
--> This allows a child class(subclass) to acquire the attributes and methods of a parent class(Baseclass)
this is called Inheritance

#Types of Inheritance:
1.Single
2.Multi-level
3.Multiple
4.Hierachical
5.Hybrid
'''
#super() method:
'''
-->this is used to call methods of the parent class from the child class

class parent:
    def display(self):
        print("this is parent method")
class child(parent):
    def display(self):
        super().display()
        print("This is child method")
any=child()
any.display()
'''

#Single Inheritance:
'''
This allows using single method of the class from parent class is known as single inheritance
class parent:
    def display(self):
        print("this is parent method")
class child(parent):
    def display(self):
        super().display()
        print("This is child method")
any=child()
any.display()


class parent:
    def display(self):
        print("this is parent method")
class Child(parent):
    def __init__(self):
        print("This is chinni")
x = Child()
x.display()

class parent:
    def display(self):
        print("this is parent method")
class Child(parent):
    def __init__(self):
        super().__init__()
        print("This is chinni")
x = Child()
x.display()

'''
#Multiple Inheritance:
#-->A child class inherits from more than one parent class..
'''
class parent1:
    def skill_1(self):
        print("Father: hard working")
class parent2:
    def skill_2(self):
        print("Mother:Home maker")
class child(parent1,parent2):
    def skills(self):
        print("child:coding")
ob=child()
ob.skill_1()
ob.skill_2()
ob.skills()


class name:
    def detail_name(self):
        print("my name is M.Chinni")
class age:
    def detail_age(self):
        print("I am 21 years old")
class location:
    def detail_loc(self):
        print("I am from vizag")
class mail:
    def detail_mail(self):
        print("email id: chinni@gmail.com")
class Detail(name,age,location,mail):
    def detail(self):
        print("here my details")
k=Detail()
k.detail()
k.detail_name()
k.detail_age()
k.detail_loc()
k.detail_mail()
'''
#Multi-level inheritance
'''
-->This occurs when a class inherits from a child class, creating a grandparent-->parent-->child in this
structure.
'''

class grandparent:
    def show_grandparent(self):
        print("I'm Grandparent")
class parent(grandparent):
    def show_parent(self):
        print("I'm parent")
class child(parent):
    def show_child(self):
        print("I'm child")
obj=child()
#obj.show_grandparent()
#obj.show_parent()
#obj.show_child()

'''
class mobile:
    def system_update(self):
        print("latest version updated")
class mobileapps(mobile):
    def apps(self):
        print("apps installed")
class data(mobileapps):
    def storage_data(self):
        print("Data is more usage for apps downloaded")
j=data()
j.system_update()
j.apps()
j.storage_data()
'''
#Hierachical
'''
-->This occurs when multiple child classes inherits from a single parent class, this process
is called Hierachical

class Parent:
    def parent(self):
        print("I am parent")
class Child1(Parent):
    def child1(self):
        print("I am 1st child")
class Child2(Parent):
    def child2(self):
        print("I am 2nd child")
class Child_3(Child1,Child2):
    def child(self):
        print("I am a child")
k=Child_3()
k.parent()
k.child1()
k.child2()
k.child()
'''

#Hybrid Inheritance
'''
-->This is a combination of two or more types of inheritance,such as single,multiple,multi-level and
hierachical all this in a single class
'''
#class grandparent:
#    def show_grandparent(self):
#        print("I am Grandparent")
class Parent:
    def parent(self):
        print("I am parent")
class Child1(Parent):
    def child1(self):
        print("I am 1st child")
class Child2(Parent):
    def child2(self):
        print("I am 2nd child")
class Child_3(Child1,Child2,grandparent):
    def child(self):
        print("I am inherited from grandparent class and child1,child2")
k=Child_3()
k.show_grandparent()
k.parent()
k.child1()
k.child2()
k.child()



















