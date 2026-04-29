class _person:
    def person__(self,name,edu,age):
        self.name=name
        self.edu=edu
        self.age=age
    def details(self):
        return f"Name:{self.name} Education:{self.edu} Age:{self.age}"
class student(_person):
    def __init__(self,name,edu,age,student_id,student_course):
        super().person__(name,edu,age)
        self.student_id=student_id
        self.student_course=student_course
    def display_info(self):
        print("-----Student Details-----")
        super().details()
        #print(f"Name:{self.name} Education:{self.edu}")
        #print(f"Age:{self.age}")
        print(person__.details())
        print(f"Student ID:{self.student_id}")
        print(f"Course:{self.student_course}")
s1=student("chinni","B.tech",21,"1234","Python full stack")
s2=student("maha","Degree",22,"1203","Java full stack")
s1.display_info()
'''
class professor(_person):
    def __init__(self,professor_name,professor_id,professor_course):
        #super().__init__(name,age)
        self.professor_name=professor_name
        self.professor_id=professor_id
        self.professor_course=professor_course
    def display_info_details(self):
        print("\n-----Professor Details-----")
        #super().display_info()
        print(f"Name:{self.professor_name}")
        print(f"professor ID:{self.professor_id}")
        print(f"Course:{self.professor_course}")
s1=student("chinni","B.tech",21,"1234","Python full stack")
s1.display_info()
p1=professor("Prakash","7846","python")
p1.display_info_details()
'''













'''
s1=student("chinni","B.tech",21,"1234","Python full stack")
s2=student("maha","Degree",22,"1203","Java full stack")
s1.display_info()
'''
'''             
p1=_person(name="chinni",edu="B.tech",age=21)
p2=_person(name="maha",edu="Degree",age=22)
print(p1.details())
print(p2.details())
'''
