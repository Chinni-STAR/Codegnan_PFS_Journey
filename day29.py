#File handling:
    file handler is an object and file to maintain several functions
    of the file such as creating , reading, writing and update also deleting the file.
#How to open a file:
    1.open()
    2.with open()
#1.open()-->This open() function takes 2 parameters and in this we have to close
the file by calling close() function after program...
    1.file name
    2.mode
#Modes: ("r","w","a","x","t")
        1."r"--read
        2."w"--write
        3."a"--append
        4."x"--create

#1."r"--read
'''
--->to read the file we will this mode and if the file doesn't exist.it will through the error
#EXAMPLE:
any = open("file.txt","r")
print(any.read())
any.close()
'''
#2."w"--write
'''
-->to write the text into file we will use this mode and it will create
-->it will overwrite new text with old text in the file
the file if it does't exist

#EXAMPLE:IF IT EXISTS
any = open("file.txt","w")
any.write("why we use this")
any.close()

#EXAMPLE:IF IT DOESN'T EXIST
any = open("tap","w")
any.write("softskills")
any.close()

'''

#3."a"--append
'''
-->to add the text the file this is used and it will create the file if it doesn't exist
-->it will write text at the end.

#EXAMPLE:
any = open("file.txt","a")
any.write("task")
any.close()
'''

#4."x"--create
'''
-->this is used to create the file , but if the file is already exists in the system it will rise an error.
'''

'''
#To read the file:
    1.read()
    2.redline()
    3.readlines()
'''
#1.read()
'''
-->this method can read the entire file chunk by chunk..
#EXAMPLE:
any = open("file.txt","r")
print(any.read())
any.close()

#EXAMPLE: also we use indexing
any = open("file.txt","r")
print(any.read(6))#length
any.close()
'''

#2.readline()
'''
-->this method can only read one line at a time
#EXAMPLE:
any = open("file.txt","r")
print(any.readline())
any.close()

#EXAMPLE:
any = open("file.txt","r")
print(any.readline(4))#length
any.close()
'''
#3.readlines()
'''
-->This method can read the entire file and return into list with each line
is one 

#EXAMPLE:
any = open("file.txt","r")
print(any.readlines())
any.close()

#EXAMPLE:
any = open("file.txt","r")
print(any.readlines(1))#using index
any.close()
'''

for removing file
import os
os.remove("file.txt")
2.with open()
