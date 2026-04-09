#lambda function()
'''
-->This is also called anonymous function
-->lambda func can take n number of arguments but have only one expression
syntax:
 lambda(keyword) arguments: expression


k= lambda so:so+10
print(k(5)) #these function takes one argument at a time.
#print(k(89,34)) #TypeError: <lambda>() takes 1 positional argument but 2 were given

k= lambda so,i:i+so
print(k(7,9))

h= lambda w,m,n:(w*n)+m #here, it can pass n number of arguments at a time and it cn pass only single expression
print(h(4,9,2)) 

#program for add,sub,mul and div using lambda function
hello=lambda w,n,k,o:(w+n)+(k+o)
print(hello(5,6,7,8))

chi=lambda i,j,l:(l-i)-j
print(chi(5,76,8))

chin=lambda y,x:(x+x)*y
print(chin(7,90))

chinn=lambda hi,hlo:hi/hlo
print(chin(35,7))
'''

#List Comprehension:
'''
-->this is offers the shorter syntax when you want to create a new list from the existing list
syntax:
    variable_name=[expression loop or condition]
'''
list=[1,3,4,5,6]
new_list=[k for k in list if k%2==0] #if expression cannot given and it shown syntax error
print(new_list)

































