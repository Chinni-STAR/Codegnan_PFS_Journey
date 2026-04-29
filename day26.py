#polymorphism
'''
-->This allows a object of different classes to be treated as instance of the same base class,with
methods behaving differently based on the actual object type.

example:len,indexing,slicing...
print(len("python"))
print(len([1,2,3]))
#print(type("python"))
'''
#Method Overloading:
'''
-->This defines multiple methods with the same name but different parameters(number,type,or order)in the
same class
'''
'''
class calculator:
    def add(self,a=0,b=0,c=0):
        return a+b+c
cal=calculator()
print(cal.add(2))
print(cal.add(7,9))
print(cal.add(5,9,7))

class calcu:
    def sub(self,n,u,m=0):
        return n-u-m
cal=calcu()
print(cal.sub(78,56))
print(cal.sub(5,1,5))
'''

#Method Overriding
'''
-->This occurs in the child class,redefining a parent class method with the same signature for runtime.
'''
'''
class animal:
    def speak(self):
        return "sound"
class dog(animal):
    def speak(self):
        return "Bark"
class cat(animal):
    def speak(self):
        return "meow"
d=cat()
print(d.speak())
'''

import pyttsx3
engine=pyttsx3.init()
class father:
    def sound(self):
        return "waste fellow"

class mother(father):
    def sound(self):
        engine.say(sound)
d=father()
d.sound()


import pyttsx3
engine=pyttsx3.init()
def audio_text(text):
    engine.say(text)
audio_text("hello,i am your assiatant")

#Operator Overloading
'''
-->This is customizes operator like +,- for user-defined classes by implementing 
'''
class someone:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    #def __add__(self,any_):
        #return someone(self.a+any_.a,self.b+any_.b)
    def __mul__(self,any_):
        return someone(self.a*any_.a,self.b*any_.b)
    def __str__(self):
        return f"{self.a},{self.b}"
d=someone(3,4)
a=someone(8,9)                
print(d*a)


#Data Abstraction
'''
-->This hides complex implementation details,exposing only esstential features via abstract class
or interface.
'''
from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14 *self.radius **2
c=circle(5)
print(c.area())


























