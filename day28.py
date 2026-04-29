#Handling Errors
'''
try block
except block
else block
finally block
'''
#Try block
'''
-->The try block will test a block of code for errors.
e.g:
try:
    a=9
    print(b)
'''
#except block
'''
-->This block will take care of any errors
e.g:
try:
    print(a)
except:
    print("This block can handle error")

try:
    a=2
    b=4
    print(a+c)
except NameError:
    print("This can shown the error")
'''
#else block
'''
-->else keyword to define a block of code to be executed if no error were raised
e.g:
try:
    a=9
    b=10
    print(a+b)
except:
    print("error here")
else:
    print("No error in the code")
    
try:
    name="maha"
    print(name)
except:
    print("this block is error")
else:
    print("No error")

try:
    a=10
    b=0
    print(a/b)
except:
    print("This block has errors")
'''
#finally block
'''
-->This block will execute either try block have any error or no error
e.g:
try:
    a=9
    b=10
    print(a+b)
except:
    print("error here")
else:
    print("No error in the code")
finally:
    print("the try-except block is finished")

try:
    a=10
    b=0
    print(a/b)
except:
    print("error here")
finally:
    print("This block has errors")
'''

try:
    n1=int(input("enter the num1:"))
    n2=int(input("enter the num2:"))
    res=n1/num2
    print(res/n)
except ValueError:
    print("plz enter the valid number")
except ZeroDivisionError:
    print("cannot divided by Zero")
except NameError:
    print("name cannot be defined")
else:
    print(f"Result:{res}")
finally:
    print("program is executed")

















