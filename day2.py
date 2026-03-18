

'''
a=1
b=12
a=25
#python is dynamically typed,you need not define the datatypes also
#only recent value to the variable with same name pointed
print(a)

#1a23 = 4 #syntax error
#@weef=9 #syntax error
name = "chinni"
location ="vizag"
age=20
emailid= " chinni@gmail.com"
email_id = "chinni@gmail.com"
print(name,location, emailid)

# how to assign multiple values to a variable
#a,b,c=21 type error
a, ab, abc=24,56,67
print(a,ab,abc)
print(a)
print(ab)
print(abc)

# assign same values to multiple variables
x=y=z=34
print(x,y,z)

#keywords are reserved words whivh will be specific usage
#there are 35 keywords in python
#never use keywords as identifiers

#if=35
#lambda="sya"
#False=0 #cannot assign
# python is case sentitive
false=78
Not=90

#identifiers are names given to variables,functions, classes,objects.....
#literals are fixed values to a identifier
name= 'sfejnd'
age=35

#name is identifier,20 is literal
#single line comments-- #
#Multi line comments - # strat end with triple quotes
'''
'''
# built in datatypes --> Numeric,boolean, Collections

#Numeric datatypes - int,float,complex
#int - count, values,quantities
#float - temperature, percentage, price
#complex - specific conversions(real and imaginary)

count = 49
#type coneversion it show what type of datatype is used to variable
print(count)
print(type(count))

price=456.78
print(price)
print(type(price))

value=2+5j #In math, we write imaginary value i but its purpose code lang j
print(value)
print(type(value))


j3=25
value = 2+j3
print(value)
print(type(value))

#typecasting -- converting one type to another
#int - float,complex

age = 34
print(type(age))
b=float(age)
print(b)
print(type(b))
c = complex(age)
print(c)
print(type(c))


#float - int,complex

a=56.56
print(type(a))
b= int(a)
print(b)
print(type(b))
c=complex(a)
print(c)
print(type(c))

#complex
f=2+5j
print(f)
print(type(f))
b=int(f) complex to int & float is not possible # type error
print(b)
c=float(f)
print(c)
'''
#boolean datatype - validation- True/False
'''
a=True
print(a)
print(type(a))

#typeconeversion of bool

b=int(a) # True by default value of 1 and false is 0
print(b)
print(type(b))
c=float(a)
print(c)
d= complex(float(int(False)))
print(d)
print(type(d))
f=56
g=78
print(f+a+g)
'''
'''
#input -- input()/output -- print()
a=5
print(a)

a=input("enter the value:") #any input but result as str
print(a)
print(type(a))
a=int(input("enter the value:")) #only integer input
print(a)
print(type(a))

b=float(input("enter value:"))
print(b)
print(type(b))

'''
 #Now let work on a simple case study using above -- fee calculator
'''
#details of the student
name=input("enter name")
print("-------")
admission_fees=int(input("enter the admission fee"))
tutition_fees=float(input("enter the tutition fee"))
hostel_fees=float(input("enter the hostel fee"))
#calculate the total fees
total_fees=admission_fees+tutition_fees+hostel_fees
print("student name:"+name)
print("total_fees is :",total_fees)
'''
a,b=5,4
print(a,b)
print(a,b,sep='\t') #seperate=sep
print(a,b,sep='---->')
print(a,b,sep='\n')






























