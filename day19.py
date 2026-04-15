#Generators
'''
-->This is a special type of function that return an ITERATOR which one at a time
here we use yield instead return

#yield
-----
-->it will take a pause and again resume, this is not a normal keyword can not be used in normal functions.
-->This is used to produce a value and pause execution.

#Next()
-------
--->This is used to get next value from a generator
--->When the value is finished,it will stop the iterator
'''
'''
def my_generator():
    yield 1
    yield 2
    yield 3
am =my_generator()
print(next(am))
print(next(am))
print(next(am))
'''
'''
def squaregenerator(n):      
    for i in range(n):
        yield i*i
for v in squaregenerator(7):
    print(v)
'''

'''
def odd_gen(n):
    for i in range(n):
        if i%2!=0:
            yield i
for j in odd_gen(20):
    print(j)
    
def even(n):
    for i in range(n):
        if i%2==0:
            yield i
for k in even(12):
    print(k)
'''
def my_generator():
    yield "Chinni"
am =my_generator()
print(next(am))


import



































