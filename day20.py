#Modules
'''
-->A Module in a python is simply file that contain python code(functions,variable,classes)
-->To use modules,we have to use a keyword called import before the modules
'''
#Types of Modules:
'''
1.built-in or Inbuilt:
-->Already these are comes with installation and they are ready to use in the program.
-->This is developed by the developer
-->it completed with python(math,os,random....)
syntax:
    import(keyword) module_name
    module_name.functionality

2.user-define modules
-->this is developed by the user or programmer inside a file or python code and used by called import with filename.
syntax:
   import(keyword) file_name
   file_name.functionality
'''
'''
import module
print(module.add(4,5))
print(module.mul(6,5))
print(module.sub(97,73))

import day1
print(day1)

import module
print(module.name)
print(module.n+1)
print(module.prime(34,0)) 
print(module.prime(23,0))
'''
import math
print(math.pow(2,4))
print(math.sqrt(36))

import random
print(random.randint(2,24))
attempts=3
while attempts>0:
    for i in range(attempts):
        guess=input("enter the number:")
        if guess == random:
            print("you won")
        else:
            print(f"remaining chances:{attempts-1}")
            attempts -=1
            print("wrong guess")
