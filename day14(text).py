'''
#Dictionary - end with {}
#key:value

any={"name" : "chinni", "pin" :3456}
print(any)


#logical operator-
#and: two conditions are true it becomes output as true
if 10<5 and 10>20:
    print("true")
else:
    print("false")
#or: any one condition is true it becomes output as true
if 3>4 or 2<3:
    print("true")

#prime number
num=int(input("enter the number:"))
value=0
for j in range(1,num+1):
    if num%j==0:
        value+=1
if value == 2:
    print("prime")
else:
    print("not prime")

#palindrone
t=input("enter the text")
c=""
for i in t:
   c=i+c #c=c+i
if c == t:
    print("palindrone")
else:
    print("not palindrone")
'''
'''
#fibonacci series
val=int(input("enter the number:"))
a=0
b=1
print(a,b)
for i in range(val):
    c=a+b
    a=b
    b=c
    print(c)
'''
'''
week -1

python is dynamic typed language and interpreted language

mutable -- we can modify the data values directly
immutable -- not modify directly values but it modify after executed code e.g:string,list,tuple

== --> assign direct values
is --> it is object and values has same location or not ,it check memory location.
'''
#swap numbers
'''
a=int(input("enter the number1:"))
b=int(input("enter the number2:"))
#a=a+b
#b=a-b
#a=a-b
a,b=b,a
print(f"after swapping two numbers of a,b is {a} and {b}")

#leap year
#--> 4% ==0 and 100%!=0 or 400% ==0

year=int(input("enter the year:"))
if (year%4==0 and year%100!=0) or year%400==0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

#eligible to vote or not
x=int(input("enter the age:"))
if x>18:
    print(f"you are eligible to vote")
else:
    print(f"you're not eligible to vote and you can wait {18 - x} years")
'''

#compound interest



text=input("enter the text:")
count=len(text.split())
print(count)













