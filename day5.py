#Datatypes
'''
--> String - string is collection of characters,which representation by " " or '' and we can access
the using indexing(string can also allow negative indexing) and also slicing, this also immutable,
where i could not able to modification on that particular variable..
#it used to put sequence of charcters btw " "or ' '

any="python programming"
#indexing
#print(any[7,8,9]) #TypeError: string indices must be integers, not 'tuple'
#print(any[78])
print(any[7])

#slicing
print(any[7:13])
print(a+ny[2:7])
print(any[0:19])

#mutable: List , immutable: Tuple
any="python programming"
so= any.replace("python", "java")
#print(any)
print(so) 
#print(any[-6])
#print(30)#IndexError: string index out of range
'''
'''
a_day="I am Chinni from Vizag and python full stack trainee at codegnan"
#print(f"my name is {a_day[5:12]}")
#print(f"my name is {a_day[-4:-2]}")
print(f"my name is {a_day[::-1]}")
'''

 #len() ,ethod is used to get char present in the string or find the length of the string
'''
a_day="I am Chinni from Vizag and python full stack trainee at codegnan"
print(len(a_day))
'''
'''
a_day="123"
num = int(a_day)
print(type(num))
'''
'''
Note:we can convert a string into integer , if the contain only integer values....
'''
'''
some = "234"
num = int(some)
print(type(num))

some = "my name is chinni"
print(some.split(" "))


'''

'''
METHODS OS STRINGS
------------------
split()--->remove space, and the is in the list[] it will give the separated thing in each index
SYNTAX----> variable_name.split("substring")

some = "my name is chinni"
print(some.split())
#print(some.split("chinni"))
#print(some.split("i"))
'''
'''
#lower()----> this is used to convert all letters to lower case
#SYNTAX----->variable_name.lower()
some = "My namE Is ChInni"
print(some.lower())

some = "my name is chinni"
print(some.split("jai"))

#UPPER()-----> converts the lowercase letters into uppercase letters
#SYNTAX---->variable_name.upper()
#EXAMPLE
some = "My namE Is ChInni"
print(some.upper())

#replace() --> used to replace old str with the new string or some of word or sentence
#SYNTAX---->variable_name.replace("old string","new string")

some = "python is a programming language"
print(some.replace("programming", "norml"))
'''
'''
some="python is a programming language"
if "lan" in some:
    print("Yes it is there")
else:
    print("No it is not there")
'''






























