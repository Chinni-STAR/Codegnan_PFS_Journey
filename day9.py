'''
text = input("enter your lines")
vowels = 0
conso = 0
space = 0
for j in text:
    if j in "AEIOUaeiou":
        vowels += 1
    elif j == " ":
        space +=1
    else:
        conso +=1
print(vowels)
print(conso)
print(space)
'''
'''
#without consantants how to count the vowels and consantants
any = input("enter your lines:")
vowels = 0
space = 0
for j in any:
    if j in "AEIOUaeiou":
        vowels += 1
    elif j == " ":
        space +=1
print(f"this is count of all vowels in string {vowels}")
print(f"this is count of all spaces in string {space}")
print(f"this is count of all conso in the string {len(any)-(vowels+space)}")
'''
'''
a = 10#normal variable
print(a)
for i in range(1,10):
    print(i)
for i in range(1,10):#"i" is a initial variable also we will not get error in initial variable
    print(i)
for i in range(1,11,2):
    print(i)
'''    
# range()---> this is used to generate the numbers
#SYNTAX---->range(start,end,step)
'''
for i in range(1,11,4):
    print(i)

for i in range(0,5):
    print(i)
''' 
any = "123456"
print(int(any))
print(list(any))
print(tuple(any))

so = 12345
print(str(so))
print(float(12345))

a = [1,2,3]
bn = (str(a))
print(type(bn))
print(bn)
print(tuple(bn))

a = [(1,2),(3,4)]
print(dict(a))

a = "chinni"
print(a[::-1])
rev = "chinni"
empty = ""
for j in rev:
    empty += j 
    print(empty)

rev = "chinni"
empty = ""
for j in rev:
    empty = j + empty
    print(empty)

rev = "madam"
empty = ""
for j in rev:
    empty = j + empty
if empty == rev:
    print(f"this is palin {rev}")
else:
    print(f"this is no palin {rev}")

rev = "*****"
empty = ""
for j in rev:
    empty = j + empty
    print(empty)

rev = "*****"
empty = " "
for j in rev:
    empty += j 
    print(empty)
'''
for num in range(1,10):
    if num % 2 == 0:
        print(f"{num}:is a even number")
    else:
        print(f"{num}:is odd number")
'''
