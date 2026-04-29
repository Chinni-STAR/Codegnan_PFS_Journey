
#Constructor (__init__)
#--> A constructor is a special method used  to initialize object data __init__()
class student:
    def __init__ (self, name, ID):
        self.name = name
        self.ID = ID
        
    def display(self):
        print(self.name, self.ID)
Stu_1 = student("chinni", 12345)
Stu_1.display()

#Access Specifiers
'''
1.public
SYNTAX --> name
we can use anywhere in  the program
2.protected
SYNTAX --> _name #single underscore
This is only for the internal use
3.private
SYNTAX --> __name #double underscore
this one is restricted
'''
#self
#--> This keyword is instance variable and unique for each object

class some:
    def __init__(self):
        self.public = "public"
        self.protected = "protected"
        self.private = "private"

any = some()
print(any.public)
print(any.protected)
print(any.private)
