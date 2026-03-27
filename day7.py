'''
print(9+10)
print("python"+"programming")
print([1,7]+[55,90])
'''
#concatenation------> this is nothing but ,a (+) behavi..
#CASE_1--->Integers--->this will act as addition for int
#EX---->
'''
print(9+10)
'''
#case_2---> cancatenation could not able to add two different types like string to int
#for other datatypes we have to use same type)this (+) act as contination.
#EX-->
'''
print([1]+"programming")#TypeError: unsupported operand type(s) for +: 'int' and 'str'
#TypeError: can only concatenate list (not "str") to list
'''
'''
print([1,55,0]+"pot")
'''
#tuple()---> is a collection of different datatypesand this is represented by (),separated by (,).

'''
thing = (1,"jai",[1,45],(6,89))
print(thing[1][0])#using indexing

'''
'''
thing = (12,89,"python",(23,"jai",[67,"python is a language",(7,8)],[8,("python",[34,9])]))
print(thing[3][2][1][9])
'''
num = 33
num_2 = 6
print(f"before swapping num = {num} and num_2 = {num_2}")
num,num_2 = num_2,num
print(f"after swapping num = {num} and num_2 = {num_2}")

'''
leap_year = int(input("enter year :"))
if leap_year % 4 == 0 and leap_year % 100 != 0 or leap_year % 400 == 0:
    print(f"yes {leap_year} its a leap year")
else:
    print(f"no {leap_year} its not a leap year")
'''
