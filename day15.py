'''
functions()-- this is a block of code which is reuseable
-->two types 1. built-in or In-build
             2. user defined
             
1.Built-in or In bulid
----------------------
-->they comes with program and those are already defined.
e.g..
---> print(),sum(),map()....

2.User defined
--------------
--> this is created by person who is developing or using for development

Note:
--> It start with def keyword followed by func name
--> and it has calling function
syntax:
def func_name(): #() in these what will stored is called as parameters e.g:(a,b) or (num)
   ----
   ----
fun_name() #()-arguments
'''
'''
a=int(input("enter the number:"))
def evenorodd(a): #definition of function
    if a % 2==0:
        print("even")
    else:
        print("odd")
evenorodd(a) #calling function

def evenorodd(a=2):
    if a % 2==0:
        print("even")
    else:
        print("odd")
evenorodd(a=2)

u=int(input("enter the number"))
def prime(v): # should store valued another variable name also
    print(v)
prime(u) #should assign same variable name only


num=7
count=0
def prime(Num,k):
    for j in range(1,Num+1):
        if Num % j==0:
            k+=1
    if k == 2:
        print("prime")
    else:
        print("Not prime")
prime(num,count)
'''
text="chinni"
res=""
def palindrone(tex,i):
    for k in tex:
        i=k+i
    if i==tex:
        print("palindrone")
    else:
        print("not palindrone")
palindrone(text,res)


