'''
ways to pass arguments in calling function
Required Arguments :
--->The parameters and arguments should be equal or it should match same number variables in calling
   with def

n=9
n1=67
def add(num,num_1):
    print(num)
add(n,n1)
'''
'''
Default Arguments :
--->It should assigns the default values from arguments (or)
-->it will take the default values from arguments
name="chinni"
def add(name):
    print(name)
add(name="musirana")
add(name="maha")
add(name="viha")
'''
'''
#prime number using function
def prime(num,count):
    for i in range(1,num+1):
        if num%i == 0:
            count=count+1
    if count == 2:
        print(f"{num} is a prime")
    else:
        print(f"{num} is not a prime")
#num=int(input("enter the number:"))
#count=0
#prime(num,count)
prime(num=2,count=0)
prime(num=24,count=0)

#Even or odd
def evenorodd(n):
    if n%2 != 0:
        print(f"{n} is odd")
    else:
        print(f"{n} is even")
evenorodd(n=90)

def text(words,rev):
    for i in words:
        rev = i +rev
    if rev == words:
        print("palin")
    else:
        print("Not Palin")
text(words="madam",rev="")

#length of string
def text(t,k):
    for i in t:
        c=len(t)
        k=k+c
        print(k)
text(t="chinni",k=0)
'''
'''
#keyword arguments

def c(n1,n2,n3):
    print(f"n1={n1},n2={n2},n3={n3}")
c(n2=90,n3=8,n1=1)
'''

#varible length argument : 

def name(*art):
    print(art[0])
name(12,4,5)





















