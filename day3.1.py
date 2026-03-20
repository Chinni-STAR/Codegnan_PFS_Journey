'''
operators-> An operator is a symbol that performs an operation on one or more values(operands) and produces a result

operators are primarily used:
-- calculate values
-- compare values/ inputs
-- make decisions
-- control the progeram flow

there are major seven categories of operators
-- arithmetic opertaors
-- assignment operators
-- comparsion operators
-- membership operator (in,in not)
-- identity operator(is,is not)
-- bitwise operators
-- logical operators (and, or,not)
'''


 #Arithmetic Operators--> arithmetic operators perform mathematical operations
#+ -->addition,- -->subtraction,*-->multiplication ,/ -->division, ** --> exponent
#%-->modulus, //--> integer division
'''
a=5
b=3
print(a+b)
print(a-b)
print(a*b)
print(a/b) #return the result in float values.
print(a**b) #returns the exponential values
print(a%b) #modulus division should be returns remainder
print(a//b) #INTEGER/floor division -->returns quotient discard float values
'''
'''
num1 = int(input("enter first value:"))
num2 = int(input("enter second value:"))
result = (num1+num2)*4
print("The result is:",result) #standard notation

#f-string notation
print(f'Num1 is {num1}')
print(f'Num2 is {num2}')
print(f'the result of {(num1+num2)*4}')
print(f'The result of {num1} and {num2} is: {result},{num1*num2}')
print(f'the result is {result}')

#assignment operators
#-->= assign ,=+ addition assignment, -= substract assignment, *= ,/=,%=,//=, **=

#They are majorly used for code repetition in application usage
used as frequency,counter,

a = 4
b = 3
a +=2 #--> a= a+2
print(a)
b +=a
print(b)
a -=3 #3
print(a)
b -=a #6
print(b)
print(f' the updated values of a and b are {a} and {b}')
b *=a #b=6*3=18
print(b)
a **=b 
print(a)


#Comparsion or relational operators --> They always return the boolean values (true/false)
#== is equal to, != is not equal to
#< less than, > greater than, >=,<=
#to validate the logic values

a=int(input('enter the value:'))
b=int(input('enter 2nd value:'))
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a>=b)
print(a<=b)
#membership operator --> they check for the existence of an object in a collection
#collection --> in , not in

a= "codegnan"
print(type(a))
#print('d' in 'a')
print('a' in a)
print('z' in 'saketh')
print('z' not in 'codegnan')

b=[12,6,3,5]
c=int(input('enter the value'))
print(c)
#print(c in [15,78,56,86]) 
print(c in b)
print(c not in b)


#Logical operators --> They are used to combine multiple conditions
# and --> if all conditions or cases are satisfied it return true value
# or --> if one condition is satisfied it return true value,not

age= int(input('enter the age:'))
vote_right=True
print(age>=18 and vote_right)
print(age>18 or vote_right)
print(not vote_right)


#Identity operators --> they check the memory location and validate we used
#(id) function it is different from == operator ->is ,is not

a=[1,2,4]
b=[1,2,4]
print(a==b)
print(id(a)) #return the identity of an object 
print(id(b))
print(a is b)
print(a is not b)

d=[1,2]
print(d)
print(id(d))
c=b #return the value of c is [1,2,4], it address will be same as b bcz it assign the same value
print(c)
print(id(c))
print(c is b)
'''

#bitwise operators -->They check the binary values
#bitwise AND &,Bitwise OR | perform bitwise operator
#we get the result(return the binary conversion)

print(5&3)
print(bin(5)) #returns binary number

#Task -->Now you have all operators create a Checker Task -->arithmetic,assignment,membership,comparsion
















