'''
num=5
for j in range(num):
    for i in range(j):
        print("*",end="")
    print()

num=int(input("enter the limit:"))
for j in range(num):
    for i in range(j):
        print("a",end="")
    print()

num=int(input("enter the limit:"))  e.g:0
for j in range(num):                    01
    for i in range(j):                  012
        print(i,end="")
    print()

num=int(input("enter the limit:"))
for j in range(num):
    for i in range(j):
        print(j,end="")
    print()


num=int(input("enter the limit:"))
for j in range(num):
    for i in range(num): #to get all rows and columns like a square
        print("*",end="")
    print()


num=int(input("enter the limit:"))
for j in range(num):
    for i in range(num-j): #to get reserved way pattern and start with highest valued in the pattern
        print("*",end="")
    print()

#pyramid pattern - like triangle way
num=int(input("enter the limit:"))
for j in range(num):
    print(" "*(num-j),end="")
    for i in range(j+1):
        print("*",end=" ")
    print()
'''
'''
#left angle triangle
     *
    **
   ***
  ****
 *****
num=int(input("enter the limit:"))
for j in range(num):
    print(" "*(num-j),end="")
    for i in range(j+1):
        print("*",end="")
    print()
'''

num=int(input("enter the limit:"))
for j in range(num):
    print(" "*(num-j),end="")
    for i in range(j+1):
        print("*",end="")
    print()
