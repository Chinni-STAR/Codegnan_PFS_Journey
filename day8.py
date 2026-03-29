#dictionaries----> we can store data as key : value
#HERE:
#keys are unique and we can only give #immutable datatypes in keys
#values---> we give all datatypes (mutable and immutable)
#represented by{}
'''
hello= {"name" : "Chinni",
       "Name" : 9,
       (9,0):0,
       [5,9]:78}#unhashable type: 'list'
print(hello)
'''
#methods
#------>
#keys() --> this method is used to get all keys from dict
#values() --->  this method is used to get all values from the dict
#clear()--->this method is used to delete the dict
'''
hlo = {"name":"chinni",
       "role":"student",
       "rol":998}
print(hlo.keys())
print(hlo.values())
'''
#clear()--->this method is used to delete the dict
'''
hlo = {"name":"chinni",
       "role":"student",
       "rol":998}
print(hlo.clear())
print(hlo)
'''
#set{}---> is a unordered collection with and it never allow duplicates
'''
any = {1,2,3,4,4}
print(any)
'''
#methods---->
#union()----this is used to add or get 2 different sets without duplicated
#intersection()---- this method is used to find out common items
#difference()---- this method is used to find the difference once from the 2nd set
'''
any = {6,7,8,9,0}
so = {3,9,8,1}
print(any.union(so))
print(any.intersection(so))
print(any.difference(so))
'''
#pop()---->it removes the any item in the set#remove()
'''
any = {6,7,8,9}
so = {3,9,8,1}
any.pop()
print(any)


accounts = {"chinni": "1234",
            "boo": "5678"}
name = input("Enter your name: ")
pin = input("Enter your 4-digit PIN: ")
if name in accounts and accounts[name] == pin:
    print(f"Success! Welcome back, {name}.")
else:
    print("Login failed. Check your name or PIN.")
'''
'''
code = {"banana":"yellow",
        "apple":"red"}
fruit = input("enter the fruit :")
colour = input("enter the colour :") 
if fruit in code and code[fruit] == colour:
    print(f"yes its matched, {fruit}.")
else:
    print("not matched.")
'''
